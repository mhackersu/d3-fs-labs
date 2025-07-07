# Cloud Run Function
```
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/cloudrun-example

gcloud run deploy cloudrun-example \
  --image gcr.io/YOUR_PROJECT_ID/cloudrun-example \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```