# UrbanPulse AI — Run Notes

## How to Run on Kaggle

1. **Upload the notebook**
   - Go to [kaggle.com](https://kaggle.com) → New Notebook → Upload
   - Upload `UrbanPulse_AI_MultiCity_Urban_Growth_Intelligence_Om_Choksi.ipynb`

2. **Enable Internet**
   - On the right sidebar → Settings → **Internet** → ON

3. **Accelerator**
   - GPU is optional (not required). The notebook runs fine on CPU.
   - If using GPU, set: Settings → Accelerator → GPU (T4 x2)

4. **Earth Engine Authentication**
   - You need a Google Earth Engine account (free).
   - When the notebook runs the authentication cell, follow the link, log in, and paste the token.
   - Alternatively, pre-authenticate and upload the token as a Kaggle Secret:
     - Save the token under Kaggle Secrets with key `GEE_TOKEN`
     - The notebook will automatically use it if available.

5. **Run all cells**
   - Click **Run All** (or run cell-by-cell to monitor progress)
   - Expected runtime on Kaggle CPU: **~15–15 min** (mostly GEE composite building and sampling)
   - Expected runtime on Kaggle GPU: **~10–12 min** (GPU helps only sklearn/XGBoost training)

## Outputs

All outputs are saved to two directories created in the notebook's working directory:

| Directory | Contents |
|-----------|----------|
| `urbanpulse_outputs/` | CSVs, PNG charts, confusion matrices, JSON summaries, API-ready JSONs |
| `urbanpulse_models/` | joblib model artifacts (RF, XGBoost, KMeans, scalers) |

### Key output files to check:
- `urbanpulse_outputs/{CITY}_city_summary.json` — Overall growth stats
- `urbanpulse_outputs/{CITY}_classification_metrics.csv` — Model performance
- `urbanpulse_outputs/{CITY}_predictions_quarterly_2026_2030.csv` — Future predictions
- `urbanpulse_outputs/{CITY}_sprawl_clusters.csv` — KMeans sprawl analysis
- `urbanpulse_models/{CITY}_best_classifier.joblib` — Deployable model

## What to Send Back for Review

After running, check these items:

- [ ] Notebook ran without errors (all cells completed)
- [ ] `urbanpulse_outputs/` directory exists with files
- [ ] `urbanpulse_models/` directory exists with `.joblib` files
- [ ] Final validation cell shows ✅ (12/12 checks passed)
- [ ] City summary JSON has reasonable numbers (not zeros or nulls)
- [ ] Forecast plot is generated (shows historical + predicted trend)

Zip and share:
```
urbanpulse_outputs/
urbanpulse_models/
UrbanPulse_AI_MultiCity_Urban_Growth_Intelligence_Om_Choksi.ipynb
```

## Troubleshooting

| Problem | Likely fix |
|---------|------------|
| Earth Engine auth fails | Re-run auth cell; ensure Internet is ON |
| No images found for certain year | GEE coverage varies; notebook skips gracefully |
| GHSL validation fails | GHSL dataset version may change; notebook continues |
| Dynamic World unavailable | Normal; notebook falls back to rule-based labels |
| Out of memory | Reduce `SAMPLES_PER_YEAR` in config from 4000 to 2000 |
