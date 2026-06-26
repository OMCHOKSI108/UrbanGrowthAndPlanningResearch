import json, os, math
from flask import Flask, render_template, jsonify, send_from_directory
import folium
import pandas as pd

app = Flask(__name__)

DATA_DIR = os.path.join(os.path.dirname(__file__), "urbanpulse_outputs")
API_DIR = os.path.join(DATA_DIR, "api_ready")
CITY = "Ahmedabad"


def load_json(path):
    with open(path) as f:
        return json.load(f)


def load_csv(path):
    return pd.read_csv(path)


def city_bounds():
    c = load_json(os.path.join(API_DIR, "cities.json"))
    for ci in c:
        if ci["name"] == CITY:
            return ci["bbox"], ci["center"]
    return [72.45, 22.9, 72.7, 23.15], [23.025, 72.575]


# ── Routes ──


@app.route("/")
def index():
    summary = load_json(os.path.join(API_DIR, f"{CITY}_summary.json"))
    bbox, center = city_bounds()

    m = folium.Map(location=center, zoom_start=11, control_scale=True)

    folium.Rectangle(
        bounds=[[bbox[1], bbox[0]], [bbox[3], bbox[2]]],
        color="red",
        fill=True,
        fill_opacity=0.08,
        weight=2,
        popup=f"<b>{CITY} Study Area</b><br>{summary['city_description']}",
    ).add_to(m)

    folium.Marker(
        location=center,
        popup=folium.Popup(
            f"""
            <div style="font-family:sans-serif;min-width:220px">
                <h4>{CITY}</h4>
                <b>Built-Up 2017:</b> {summary['builtup_2017_sqkm']} km²<br>
                <b>Built-Up 2025:</b> {summary['builtup_2025_sqkm']} km²<br>
                <b>Predicted 2030:</b> {summary['predicted_2030_sqkm']} km²<br>
                <b>CAGR:</b> {summary['cagr_percent']}%<br>
                <b>Risk Score:</b> {summary['sprawl_risk_score']}/100<br>
                <b>Model:</b> {summary['model_selected']}<br>
                <b>Validation:</b> {summary['validation_status']}
            </div>
            """,
            max_width=300,
        ),
        icon=folium.Icon(color="red", icon="info-sign"),
    ).add_to(m)

    clusters = load_json(os.path.join(API_DIR, f"{CITY}_sprawl_clusters.json"))
    colors = ["#e74c3c", "#2ecc71", "#f39c12", "#3498db"]
    for cl in clusters:
        folium.CircleMarker(
            location=[center[0], center[1]],
            radius=10 + cl["count"] / 200,
            color=colors[cl["cluster_id"] % len(colors)],
            fill=True,
            popup=f"<b>{cl['label']}</b><br>Pixels: {cl['count']}<br>NDBI: {cl['ndbi_mean']:.3f}<br>NDVI: {cl['ndvi_mean']:.3f}",
        ).add_to(m)

    folium.LayerControl().add_to(m)

    map_html = m._repr_html_()
    return render_template("index.html", map_html=map_html, summary=summary)


@app.route("/predictions")
def predictions():
    q = load_json(os.path.join(API_DIR, f"{CITY}_predictions.json"))
    summary = load_json(os.path.join(API_DIR, f"{CITY}_summary.json"))

    years = sorted(set(r["Year"] for r in q))
    yearly = []
    for y in years:
        qs = [r for r in q if r["Year"] == y]
        avg = sum(r["Predicted_Area_sqkm"] for r in qs) / len(qs)
        yearly.append({"year": y, "avg_km2": round(avg, 4)})

    labels = [f"{r['Year']} Q{r['Quarter']}" for r in q]
    values = [r["Predicted_Area_sqkm"] for r in q]
    historical = {
        "2017": summary["builtup_2017_sqkm"],
        "2025": summary["builtup_2025_sqkm"],
    }

    return render_template(
        "predictions.html",
        quarterly=q,
        yearly=yearly,
        labels=json.dumps(labels),
        values=json.dumps(values),
        historical=historical,
    )


@app.route("/clusters")
def clusters():
    clusters_data = load_json(os.path.join(API_DIR, f"{CITY}_sprawl_clusters.json"))
    summary = load_json(os.path.join(API_DIR, f"{CITY}_summary.json"))
    return render_template("clusters.html", clusters=clusters_data, summary=summary)


@app.route("/metrics")
def metrics():
    metrics_data = load_json(os.path.join(API_DIR, f"{CITY}_model_metrics.json"))
    return render_template("metrics.html", metrics=metrics_data)


@app.route("/outputs/<path:filename>")
def outputs(filename):
    return send_from_directory(DATA_DIR, filename)


# ── API Routes ──


@app.route("/api/summary")
def api_summary():
    return jsonify(load_json(os.path.join(API_DIR, f"{CITY}_summary.json")))


@app.route("/api/predictions")
def api_predictions():
    return jsonify(load_json(os.path.join(API_DIR, f"{CITY}_predictions.json")))


@app.route("/api/clusters")
def api_clusters():
    return jsonify(load_json(os.path.join(API_DIR, f"{CITY}_sprawl_clusters.json")))


@app.route("/api/metrics")
def api_metrics():
    return jsonify(load_json(os.path.join(API_DIR, f"{CITY}_model_metrics.json")))


@app.route("/api/cities")
def api_cities():
    return jsonify(load_json(os.path.join(API_DIR, "cities.json")))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
