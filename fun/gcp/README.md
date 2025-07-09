# Cloud Run Function

Install the GCP [CLI](https://cloud.google.com/sdk/docs/install#deb)

#### Initialize CLI

```
gcloud init
```

#### Enable the Cloud Run Admin API and Cloud Build API

```
gcloud services enable run.googleapis.com \
    cloudbuild.googleapis.com
```

```

```

```
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/cloudrun-example

gcloud run deploy cloudrun-example \
  --image gcr.io/YOUR_PROJECT_ID/cloudrun-example \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```