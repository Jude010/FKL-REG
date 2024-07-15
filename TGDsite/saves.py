from flask import Blueprint ,render_template , session
from TGDsite.db import connect 

bp = Blueprint('saves' , __name__ , url_prefix='/saves')

@bp.route('/load_saves')
def load_saves():
    #user = session['user']
    conn = connect.get_db_conn()
    cur = conn.cursor()

    # fetch all project names associated with current user
    #cur.execute("SELECT p.name FROM project p INNER JOIN saves s ON p.proj_id = s.proj_id INNER JOIN users u ON s.user_id = u.user_id WHERE username = '" + user + "';")
    cur.execute("SELECT * FROM project;")
    names = cur.fetchall()
    conn.close()

    names.extend(['a','b','c'])

    return render_template('load_saves.html.jinja' , names = names)

@bp.route('/display_save', methods=['POST'])
def display_save():
    
    return None