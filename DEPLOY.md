# Deploy to Render

Two ways to deploy the UrbanPulse AI dashboard on Render.

---

## Option 1: One-Click (render.yaml)

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/OMCHOKSI108/UrbanGrowthAndPlanningResearch)

Click the button above. Render auto-reads `render.yaml` and sets everything up.

---

## Option 2: Manual (Web UI)

### Step 1 — Push to GitHub

```bash
git push origin main
```

### Step 2 — Create Web Service

1. Go to [dashboard.render.com](https://dashboard.render.com) → **New +** → **Web Service**
2. Connect your GitHub account and select `OMCHOKSI108/UrbanGrowthAndPlanningResearch`
3. Fill in:

| Field | Value |
|-------|-------|
| **Name** | `urban-growth-map` (or any name) |
| **Runtime** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn app:app --bind 0.0.0.0:$PORT --timeout 120` |
| **Plan** | Free |

4. Under **Advanced** → **Health Check Path**: `/api/summary`

### Step 3 — Deploy

Click **Create Web Service**. Render will:

1. Clone the repo
2. Install dependencies (`pip install -r requirements.txt`)
3. Start the server with the start command
4. Provide a URL like `https://urban-growth-map.onrender.com`

Deployment takes ~2-3 minutes.

---

## Verify Deployment

Once deployed, check these endpoints:

```bash
# Dashboard homepage
curl https://urban-growth-map.onrender.com/

# API endpoints
curl https://urban-growth-map.onrender.com/api/summary
curl https://urban-growth-map.onrender.com/api/predictions
curl https://urban-growth-map.onrender.com/api/clusters
curl https://urban-growth-map.onrender.com/api/metrics
```

---

## Files Reference

| File | Purpose |
|------|---------|
| `app.py` | Flask app with 4 pages + 5 API endpoints |
| `app/templates/` | Bootstrap 5 + Chart.js HTML templates |
| `requirements.txt` | Python dependencies (Flask, gunicorn, folium, pandas, numpy) |
| `Procfile` | Render start command |
| `render.yaml` | Auto-deployment config (optional) |
| `urbanpulse_outputs/api_ready/` | JSON data files consumed by the dashboard |

---

## Notes

- **Free tier:** Render spins down after 15 min of inactivity. First request after idle takes ~30s to wake up.
- **No database needed:** The dashboard reads pre-generated JSON files from `urbanpulse_outputs/api_ready/`.
- **To add more cities:** Run the notebook for another city, copy its `api_ready/` JSONs into the repo, and update `CITY` in `app.py`.
- **Custom domain:** Render supports custom domains in the dashboard Settings.
