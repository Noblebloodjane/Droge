import psycopg2
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
                cur.execute(f"""Create table if does not exist {table_name}({','.join(columns)})""")
                conn.commit()
        conn.close()

def insert_data_table(table_name, data):
    """Populates data into table"""
    conn = get_db_conn()
    if conn:
        with conn:
            with conn.cursor() as cur:
                cur.executemany(f"""insert into {table_name} values({','.join(['%s'] * len(data[0]))}), data""")
                conn.commit()
        conn.close()
