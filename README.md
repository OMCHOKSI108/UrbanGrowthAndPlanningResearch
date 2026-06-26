# UrbanGrowthAndPlanningResearch

**Multi-City Urban Growth Prediction and Sprawl Risk Analysis** using Satellite Imagery, Machine Learning, and Google Earth Engine.

**Author:** Om Choksi

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OMCHOKSI108/UrbanGrowthAndPlanningResearch/blob/main/UrbanPulse_AI_MultiCity_Urban_Growth_Intelligence_Om_Choksi.ipynb)

---

## Goal

Build a fully automated, research-grade pipeline that:

1. **Monitors urban expansion** across Indian cities using free Sentinel-2 satellite imagery
2. **Generates pseudo-labels** for built-up areas without manual annotation (rule-based NDBI+NDVI+NDWI with confidence scoring)
3. **Trains classifiers** (Random Forest + XGBoost) to distinguish built-up vs. non-built-up land
4. **Validates against independent reference data** (GHSL 2020) for credibility
5. **Forecasts future growth** (quarterly, 2026–2030) using XGBoost time-series regression
6. **Identifies sprawl patterns** via KMeans clustering on spectral/terrain features
7. **Computes risk scores** from expansion rate, water proximity, and green-loss proxies
8. **Produces deployable artifacts** — API-ready JSONs + joblib models for FastAPI/React frontend

---

## Notebook

[UrbanPulse_AI_MultiCity_Urban_Growth_Intelligence_Om_Choksi.ipynb](UrbanPulse_AI_MultiCity_Urban_Growth_Intelligence_Om_Choksi.ipynb)

Run in Colab, Kaggle, or locally.

---

## Methodology

| Step | Description |
|------|-------------|
| 1. **Composites** | Yearly + quarterly cloud-free Sentinel-2 median composites (2017–2025) |
| 2. **Indices** | NDBI, NDVI, NDWI, water mask, mountain/slope mask |
| 3. **Pseudo-Labels** | Rule-based built-up labels with confidence scores |
| 4. **Sampling** | Stratified random sampling across years |
| 5. **Classification** | RF + XGBoost, chronological train/test (2017–2022 / 2023–2025) |
| 6. **Validation** | Against GHSL 2020 independent reference (optional) |
| 7. **Time-Series** | Quarterly built-up area calculation |
| 8. **Forecasting** | XGBoost regressor, temporal features, 2026–2030 predictions |
| 9. **Clustering** | KMeans on spectral/terrain features → 4 sprawl patterns |
| 10. **Risk Score** | Composite index: growth rate + water conflict + green loss |

---

## Cities Supported

Ahmedabad, Surat, Bengaluru, Hyderabad, Pune — switch via `SELECTED_CITY` in Section 3.

---

## Outputs

| Artifact | Location |
|----------|----------|
| Training samples | `urbanpulse_outputs/{CITY}_training_samples.csv` |
| Classification metrics | `urbanpulse_outputs/{CITY}_classification_metrics.csv` |
| Forecast metrics | `urbanpulse_outputs/{CITY}_forecast_metrics.csv` |
| Quarterly predictions (2026–2030) | `urbanpulse_outputs/{CITY}_predictions_quarterly_2026_2030.csv` |
| Yearly predictions (2026–2030) | `urbanpulse_outputs/{CITY}_predictions_yearly_2026_2030.csv` |
| Sprawl clusters | `urbanpulse_outputs/{CITY}_sprawl_clusters.csv` |
| City summary JSON | `urbanpulse_outputs/{CITY}_city_summary.json` |
| RF classifier | `urbanpulse_models/{CITY}_rf_builtup_classifier.joblib` |
| XGBoost classifier | `urbanpulse_models/{CITY}_xgb_builtup_classifier.joblib` |
| Forecast model | `urbanpulse_models/{CITY}_forecast_model.joblib` |
| KMeans model | `urbanpulse_models/{CITY}_sprawl_kmeans.joblib` |

---

## Quick Start

```bash
# Clone
git clone https://github.com/OMCHOKSI108/UrbanGrowthAndPlanningResearch.git
cd UrbanGrowthAndPlanningResearch

# Install
pip install earthengine-api geemap pandas numpy matplotlib seaborn scikit-learn xgboost joblib folium shapely

# Run
jupyter notebook UrbanPulse_AI_MultiCity_Urban_Growth_Intelligence_Om_Choksi.ipynb
```

Or open directly in [Google Colab](https://colab.research.google.com/github/OMCHOKSI108/UrbanGrowthAndPlanningResearch/blob/main/UrbanPulse_AI_MultiCity_Urban_Growth_Intelligence_Om_Choksi.ipynb).

---

## Tech Stack

- **Data:** Sentinel-2 SR Harmonized (COPERNICUS/S2_SR_HARMONIZED)
- **Platform:** Google Earth Engine (`earthengine-api`, `geemap`)
- **ML:** scikit-learn, XGBoost
- **Visualization:** matplotlib, seaborn, folium
- **Deployment:** FastAPI (planned), React + Leaflet (planned)

---

## License

MIT
