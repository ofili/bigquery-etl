from os import environ

# Google BigQuery configuration
gcp_credentials = environ.get('GCP_CREDENTIALS')
gcp_project = environ.get('GCP_PROJECT')
bigquery_dataset = environ.get('GCP_BIGQUERY_DATASET')
bigquery_table = environ.get('GCP_BIGQUERY_TABLE')
bigquery_uri = f'{gcp_project}:{bigquery_dataset}.{bigquery_table}'

# SQL database configuration
db_user = environ.get('DB_USER')
db_password = environ.get('DB_PASSWORD')
db_host = environ.get('DB_HOST')
db_port = environ.get('DB_PORT')
db_name = environ.get('DB_NAME')
db_uri = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

# Locally stored query
local_sql_folder = 'sql'
