import os
import psycopg2
from TGDsite.db import connect , save
from TGDsite.resources import readText

from flask import Flask, redirect , render_template ,session




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
        return render_template('index.html.jinja')
    
    # connect to blueprints
    from . import questions
    from . import project
    from . import login
    app.register_blueprint(questions.bp)
    app.register_blueprint(project.bp)
    app.register_blueprint(login.bp)

    
    
    return app


