# Deploy to Render (Docker)

---

## Step 1 — Push to GitHub

```bash
git add . && git commit -m "add dockerfile" && git push origin main
```

---

## Step 2 — Create Web Service

1. Go to [dashboard.render.com](https://dashboard.render.com) → **New +** → **Web Service**
2. Connect your GitHub account and select `OMCHOKSI108/UrbanGrowthAndPlanningResearch`
3. Fill in:

| Field | Value |
|-------|-------|
| **Name** | `urban-growth-map` |
| **Runtime** | **Docker** |
| **Plan** | Free |

4. Under **Advanced** → **Health Check Path**: `/api/summary`

### Important
Select **Docker** as the runtime (not Python). Render auto-detects the `Dockerfile` in the repo root and builds the image.

---

## Step 3 — Deploy

Click **Create Web Service**. Render will:

1. Clone the repo
2. Build the Docker image (`docker build -t ...`)
3. Start the container using `gunicorn app:app --bind 0.0.0.0:5000 --timeout 120`
4. Provide a URL like `https://urban-growth-map.onrender.com`

Deployment takes ~2-3 minutes for the first build.

---

## Verify

```bash
curl https://urban-growth-map.onrender.com/api/summary
curl https://urban-growth-map.onrender.com/api/predictions
```

---

## Test Locally

```bash
docker build -t urban-growth-map .
docker run -p 5000:5000 urban-growth-map
open http://localhost:5000
```

---

## Notes

- **Free tier** spins down after 15 min idle. First request after idle takes ~30s.
- **No database** — dashboard reads pre-generated JSON files from `urbanpulse_outputs/api_ready/`.
- **Add more cities** — run notebook, copy new `api_ready/` JSONs, rebuild Docker image.
