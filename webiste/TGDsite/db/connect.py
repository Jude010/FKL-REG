import psycopg2
import os

def get_db_conn():
    #connect to postgres db using environment variables
    conn = psycopg2.connect(
        host="localhost",
        database="sitedb",
        #user=os.environ["DB_USERNAME"],
        #password=os.environ['DB_PASSWORD']
        user='flask',
        password='open'
    )
    return conn