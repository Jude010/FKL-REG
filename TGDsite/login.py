from flask import Flask , render_template , Blueprint , request ,session
from TGDsite.db import connect
from TGDsite.resources import project_parts, readText

bp = Blueprint('login',__name__, url_prefix="/login")

@bp.route("/login")
def login():

    return render_template('login.html')

@bp.route("/login", methods=['POST'] )
def login_test():
    results = request.form
    conn = connect.get_db_conn()
    cur = conn.cursor()
    cur.execute("SELECT password FROM users WHERE username LIKE '" + results['username'] + "'")
    pswrd = cur.fetchone()
    conn.close()
    if pswrd == results['password']:
        session['user'] = results['username']
        return render_template('index.html')
    else :
        return render_template('login.html', fail = True)