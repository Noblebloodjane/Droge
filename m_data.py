from bs4 import BeautifulSoup
import psycopg2
import requests
from configparser import ConfigParser

def get_db_config(file='config.ini',section='postgresql'):
    """Reads database configuration from config.ini"""
    db_Parser = ConfigParser()
    db_Parser.read(file)

    db_config = {}
    if db_Parser.has_section(section):
        db_parameters = db_parameters.items(section)
        for var in db_parameters:
            db_config[db_parameters[0]] = db_parameters[1]
    else:
        raise Exception(f"db_parameters")
    return db_config

def get_db_conn():
    """Creates of database connection string"""
    db_config = get_db_config()
    try:
        conn = psycopg2.connect(**db_config)
        return conn
    except Exception as ex:
        print(f"Unable to connect to the database, read for more details:{ex}")
        return None
    
def create_tables(table_name, columns):
    """Generates tables in the database"""
    conn = get_db_conn()
    if conn:
        with conn:
            with conn.cursor() as cur:
                cur.execute()
                conn.commit()
        conn.close()
