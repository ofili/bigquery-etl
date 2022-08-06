"""BigQuery Engine."""
from sqlalchemy.engine import create_engine

from config import gcp_credentials, bigquery_uri

bigquery_engine = create_engine(
    bigquery_uri,
    credential_path=gcp_credentials,
    echo=False
)
