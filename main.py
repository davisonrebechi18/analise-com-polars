from google.cloud import storage, bigquery

def hello_gcp():
    print("✅ Ambiente GCP configurado!")
    print("→ Storage client:", storage.Client())
    print("→ BigQuery client:", bigquery.Client())

if __name__ == "__main__":
    hello_gcp()
