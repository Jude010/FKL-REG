import psycopg2
import os

def get_db_conn():
    #connect to postgres db using environment variables
    conn = psycopg2.connect(
        host="localhost",
        database="siteDB",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_USERNAME']
    )
    return conn