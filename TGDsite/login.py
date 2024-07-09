from flask import Flask , render_template , Blueprint , request ,session
from TGDsite.db import connect
from TGDsite.resources import project_parts, readText

bp = Blueprint('login',__name__, url_prefix="/login")

@bp.route("/login")
def login():

    return render_template('login.html.jinja', fail = False)

@bp.route("/login", methods=['POST'] )
def login_action():
    results = request.form
    conn = connect.get_db_conn()
    cur = conn.cursor()
    cur.execute("SELECT password FROM users WHERE username LIKE '" + results['username'] + "'")
    pswrd = cur.fetchone()
    conn.close()
    if pswrd[0] == results['password']:
        session['user'] = results['username']
        return render_template('index.html.jinja')
    else :
        return render_template('login.html.jinja', fail = True)
    
@bp.route("/register")
def register():
    return render_template('register.html.jinja' , fail = False)

@bp.route("/register" , methods=['POST'])
def register_action():
    results = request.form
    conn = connect.get_db_conn()
    cur = conn.cursor()
    cur.execute("SELECT username FROM users")
    users = []
    temp = cur.fetchall()
    for i in temp :
        users.append(i[0])


    if( results['username'] in users):
        cur.close()
        conn.close()
        return render_template('register.html.jinja' , fail = True)
    else:
        cur.execute('INSERT INTO users (username , password) VALUES ' + results['username'] + "' ,'" + results['password'] + "';")
        session['user'] = results['username']
        cur.close()
        conn.close()
        return render_template('index.html.jinja')