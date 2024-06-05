import os
import psycopg2
from TGDsite.db import connect
from TGDsite.resources import readText

from flask import Flask, render_template




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
        conn = connect.get_db_conn()
        cur = conn.cursor()
        cur.execute('SELECT guide_name FROM guide;')
        guides = cur.fetchall()
        cur.close()
        conn.close()
        #text = readText.readText(guides)
        text={1: "abc\nd",
            2: "efg\nh"}
        return render_template('index.html', texts=text)
    
    return app
