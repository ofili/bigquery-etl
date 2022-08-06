from loguru import logger
from etl.engine import bigquery_engine, postgres_engine
from etl.queries import sql_queries
from etl.client import DataClient


logger.add('logs/queries.log', format='{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}', level='INFO')


def init_pipeline():
    """Move data between BigQuery and PostgresSQL"""
    num_rows = 0
    bqc = DataClient(bigquery_engine)
    pgc = DataClient(postgres_engine)
    for table_name, query in sql_queries.items():
        logger.info(f'Fetching {table_name}...')
        rows = bqc.fetch_rows(query)
        num_rows += len(rows)
        logger.info(f'{len(rows)} rows fetched.')
        logger.info(f'Inserting {table_name}...')
        insert = pgc.insert_rows(rows, table_name, replace=True)
        logger.info(insert)
        logger.info(f'{len(rows)} rows inserted.')
    logger.info(f'{num_rows} rows fetched and inserted.')
