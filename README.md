# UrbanGrowthAndPlanningResearch

**Multi-City Urban Growth Prediction and Sprawl Risk Analysis** using satellite imagery (Sentinel-2), machine learning (XGBoost + RF), and Google Earth Engine.

**Author:** Om Choksi

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OMCHOKSI108/UrbanGrowthAndPlanningResearch/blob/main/UrbanPulse_AI_MultiCity_Urban_Growth_Intelligence_Om_Choksi.ipynb)


OPENFLASK APP : https://urbangrowthandplanningresearch.onrender.com

---

## Goal

Build a fully automated pipeline that monitors urban expansion, forecasts future growth, and produces deployable geospatial intelligence — all from free satellite imagery.

1. **Monitors urban expansion** across Indian cities using Sentinel-2
2. **Generates pseudo-labels** for built-up areas via NDBI+NDVI+NDWI rules (no manual annotation)
3. **Trains XGBoost / Random Forest** classifiers on spectral indices
4. **Validates** against independent GHSL 2020 reference data (73.5% accuracy)
5. **Forecasts quarterly growth** 2026–2030 via XGBoost time-series (R² = 0.95)
6. **Identifies sprawl patterns** through KMeans clustering
7. **Computes risk scores** from expansion rate, water proximity, and green loss
8. **Serves results** via a Flask + Folium interactive dashboard

---

## Ahmedabad Run Results

### Key Metrics

| Metric | Value |
|--------|-------|
| Built-Up 2017 → 2025 | 0.264 → 0.318 km² (+5.4%) |
| Predicted 2030 | 0.337 km² |
| CAGR | 2.35% |
| Sprawl Risk Score | 7.06 / 100 |
| **XGBoost F1** | **0.998** |
| **Forecast R²** | **0.952** |
| **GHSL Accuracy** | **73.5%** |

> **Note on classifier scores:** Both RF and XGBoost achieve very high accuracy on the test set because the pseudo-labels are derived from the same spectral indices used as features (NDBI, NDVI, NDWI). Built-up vs. non-built-up pixels have strongly separable spectral signatures. The real measure of generalisation is the **GHSL validation** (73.5% accuracy against fully independent reference data), which confirms the model learns genuine built-up patterns beyond the rule-based labels.

### Classification Performance (XGBoost — selected model)

| Accuracy | Precision | Recall | F1 | ROC-AUC |
|----------|-----------|--------|-----|---------|
| 0.998 | 0.996 | 0.999 | **0.998** | **0.999** |

### Forecast Performance (XGBoost)

| RMSE | MAE | R² |
|------|-----|----|
| 0.041 km² | 0.032 km² | **0.952** |

### GHSL External Validation (2020)

| Accuracy | Precision | Recall | F1-Score |
|----------|-----------|--------|----------|
| **73.5%** | 52.3% | 24.2% | 33.1% |

### Future Predictions (2026–2030)

| Year | Avg Predicted Area |
|------|--------------------|
| 2026 | 0.346 km² |
| 2027 | 0.338 km² |
| 2028 | 0.337 km² |
| 2029 | 0.337 km² |
| 2030 | 0.337 km² |

### Sprawl Clusters

| Cluster | Label | Pixels | NDBI | NDVI | Interpretation |
|---------|-------|--------|------|------|----------------|
| 0 | Existing Dense Urban | 1,070 | 0.103 | -0.144 | High NDBI, low NDVI — dense built-up |
| 1 | Stable Non-Urban / Low Growth | 887 | -0.178 | 0.515 | High NDVI — vegetation / agriculture |
| 2 | New Expansion / Edge Growth | 2,196 | 0.075 | 0.172 | Moderate NDBI + NDVI — recent expansion |
| 3 | Existing Dense Urban | 1,847 | 0.045 | 0.112 | Dense built-up with some vegetation |

---

## Output Visualizations

| Plot | Preview |
|------|---------|
| **Quarterly Built-Up Area** (2017–2025) | ![Quarterly Built-Up](https://raw.githubusercontent.com/OMCHOKSI108/UrbanGrowthAndPlanningResearch/main/urbanpulse_outputs/Ahmedabad_quarterly_builtup.png) |
| **Yearly Built-Up Area** | ![Yearly Built-Up](https://raw.githubusercontent.com/OMCHOKSI108/UrbanGrowthAndPlanningResearch/main/urbanpulse_outputs/Ahmedabad_yearly_builtup.png) |
| **Confusion Matrix** | ![Confusion Matrix](https://raw.githubusercontent.com/OMCHOKSI108/UrbanGrowthAndPlanningResearch/main/urbanpulse_outputs/Ahmedabad_confusion_matrix.png) |
| **Feature Importance** | ![Feature Importance](https://raw.githubusercontent.com/OMCHOKSI108/UrbanGrowthAndPlanningResearch/main/urbanpulse_outputs/Ahmedabad_feature_importance.png) |
| **Forecast Plot** (2026–2030) | ![Forecast Plot](https://raw.githubusercontent.com/OMCHOKSI108/UrbanGrowthAndPlanningResearch/main/urbanpulse_outputs/Ahmedabad_forecast_plot.png) |
| **Sprawl Clusters** | ![Sprawl Clusters](https://raw.githubusercontent.com/OMCHOKSI108/UrbanGrowthAndPlanningResearch/main/urbanpulse_outputs/Ahmedabad_sprawl_clusters_plot.png) |
| **GHSL Validation Confusion Matrix** | ![GHSL Validation](https://raw.githubusercontent.com/OMCHOKSI108/UrbanGrowthAndPlanningResearch/main/urbanpulse_outputs/Ahmedabad_ghsl_validation_confusion_matrix.png) |

---

## Interactive Dashboard

A **Flask + Folium** dashboard is included for visualizing results on an interactive Gujarat map.

![Dashboard Home Page](https://raw.githubusercontent.com/OMCHOKSI108/UrbanGrowthAndPlanningResearch/main/docs/image.png)

### API Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /` | Interactive Folium map with Ahmedabad study area + stats |
| `GET /predictions` | 2026–2030 bar chart + yearly/yearly tables |
| `GET /clusters` | Cluster table, doughnut chart, per-cluster interpretation |
| `GET /metrics` | Classification + forecast + GHSL validation metrics |
| `GET /api/summary` | City summary JSON |
| `GET /api/predictions` | 20 quarterly predictions |
| `GET /api/clusters` | Cluster centroids and labels |
| `GET /api/metrics` | All model metrics |

### Run Locally

```bash
uv pip install flask folium gunicorn pandas numpy
python app.py
```

### Deploy on Render

Push to GitHub, create a new Web Service, point to this repo. Render auto-detects the Procfile.

---

## Notebook

Run in **Colab**, **Kaggle**, or **locally**.

[UrbanPulse_AI_MultiCity_Urban_Growth_Intelligence_Om_Choksi.ipynb](UrbanPulse_AI_MultiCity_Urban_Growth_Intelligence_Om_Choksi.ipynb)

---

## Methodology

1. **Composites** — Yearly + quarterly cloud-free Sentinel-2 median composites (2017–2025)
2. **Indices** — NDBI, NDVI, NDWI, water mask + mountain/slope mask
3. **Pseudo-Labels** — Rule-based built-up labels with confidence scores
4. **Sampling** — Stratified random sampling across years for ML
5. **Classification** — XGBoost + RF, chronological split (2017–2022 train, 2023–2025 test)
6. **Validation** — Against GHSL 2020 independent reference
7. **Time-Series** — Quarterly built-up area from classification
8. **Forecasting** — XGBoost regressor with temporal features → 2026–2030
9. **Clustering** — KMeans on spectral/terrain features → 4 sprawl patterns
10. **Risk Score** — Composite: growth rate + water conflict + green loss

---

## Project Structure

```
├── UrbanPulse_AI_MultiCity_Urban_Growth_Intelligence_Om_Choksi.ipynb   # Main notebook
├── README.md
├── requirements.txt                     # Flask dashboard deps
├── Procfile                             # Render deployment
├── app.py                               # Flask dashboard
├── app/templates/                       # HTML templates
├── urbanpulse_outputs/                  # CSV, JSON, PNG outputs
│   └── api_ready/                       # JSON for dashboard API
└── urbanpulse_models/                   # .joblib trained models
```

---

## Quick Start

```bash
git clone https://github.com/OMCHOKSI108/UrbanGrowthAndPlanningResearch.git
cd UrbanGrowthAndPlanningResearch

# Install + run notebook
uv pip install earthengine-api geemap pandas numpy matplotlib seaborn scikit-learn xgboost joblib folium shapely
jupyter notebook UrbanPulse_AI_MultiCity_Urban_Growth_Intelligence_Om_Choksi.ipynb

# Or run the dashboard (after outputs generated)
uv pip install -r requirements.txt
python app.py
```

Or open in [Google Colab](https://colab.research.google.com/github/OMCHOKSI108/UrbanGrowthAndPlanningResearch/blob/main/UrbanPulse_AI_MultiCity_Urban_Growth_Intelligence_Om_Choksi.ipynb).

---

## Tech Stack

| Layer | Tools |
|-------|-------|
| Satellite Data | Sentinel-2 SR Harmonized (GEE) |
| Processing | Google Earth Engine, geemap |
| ML | scikit-learn, XGBoost |
| Viz | matplotlib, seaborn, Folium, Chart.js |
| Dashboard | Flask, Bootstrap 5 |
| Deployment | Render (Gunicorn) |

---

## License

MIT
