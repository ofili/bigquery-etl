"""Postgres engine for ETL."""
from sqlalchemy import create_engine

from config import db_uri

postgres_engine = create_engine(db_uri, echo=False)
