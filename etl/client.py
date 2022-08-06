"""Client for interacting with the ETL service."""
from sqlalchemy import MetaData, Table


class DataClient:

    def __init__(self, engine):
        self.engine = engine
        self.metadata = MetaData(bind=self.engine)
        self.table_name = None

    @property
    def table(self):
        if self.table_name:
            return Table(self.table_name, self.metadata, autoload=True)
        else:
            return None

    def insert_rows(self, rows, table=None, replace=None):
        """Insert rows into a table."""
        if replace:
            self.engine.execute(f'TRUNCATE TABLE {table}')
        self.table_name = table
        self.engine.execute(self.table.insert(), rows)
        return self.construct_response(rows, table)

    def fetch_rows(selfself, query):
        """Fetch rows from a table."""
        rows = self.engine.execute(query).fetchall()
        return rows

    @staticmethod
    def construct_response(rows, table):
        """Construct a response from a list of rows."""
        columns = rows[0].keys()
        column_names = ", ".join(columns)
        num_rows = len(rows)
        return f'{num_rows} rows inserted into {table} ({column_names})'

