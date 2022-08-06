"""Read SQL queries from file."""
from os import listdir
from os.path import isfile, join
from config import local_sql_folder


def get_local_sql_files():
    """Get local SQL files."""
    files = [local_sql_folder + '/' + f for f in listdir(local_sql_folder) if isfile(join(local_sql_folder, f)) if '.sql' in f]
    return files


def read_sql_queries():
    """Read SQL queries from file."""
    files = get_local_sql_files()
    file_contents = [open(file, 'r').read() for file in files]
    return file_contents


def get_table_names(file_names):
    """Get table names from file names."""
    tables = [f"file.split('.')[0]_stats" for file in file_names]
    return tables


def create_query_dict():
    """Create a dictionary of SQL queries."""
    file_names = listdir(local_sql_folder)
    file_contents = read_sql_queries()
    table_names = get_table_names(file_names)
    files = dict(zip(table_names, file_contents))
    return files


sql_queries = create_query_dict()
