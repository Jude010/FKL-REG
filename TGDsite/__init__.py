import os
import psycopg2

from flask import Flask, render_template

def get_db_conn():
    #connect to postgres db using environment variables
    conn = psycopg2.connect(
        host="localhost",
        database="siteDB",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_USERNAME']
    )
    return conn

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'test'
    )

    if test_config == None:
        #load from config file if it exits when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if exists
        app.config.from_mapping(test_config)

    #ensure instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    @app.route('/')
    def index():
        conn = get_db_conn()
        cur = conn.cursor()
        cur.execute('SELECT guide_name FROM guide;')
        guides = cur.fetchall()
        cur.close()
        conn.close()
        return render_template('index.html, guides=guides')
