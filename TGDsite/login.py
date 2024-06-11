from flask import Flask , render_template , Blueprint , request ,session
from TGDsite.db import connect
from TGDsite.resources import project_parts, readText

bp = Blueprint('login',__name__, url_prefix="/login")

@bp.route("/login")
def login():

    return render_template('login.html')

@bp.route("/login", methods=['POST'] )
def login_test():
    
    