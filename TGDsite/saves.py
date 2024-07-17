from flask import Blueprint ,render_template , session
from TGDsite.db import connect 

bp = Blueprint('saves' , __name__ , url_prefix='/saves')

@bp.route('/load_saves')
def load_saves():
    user = session['user']
    conn = connect.get_db_conn()
    cur = conn.cursor()

    # fetch all project names associated with current user
    cur.execute("SELECT pname FROM project p INNER JOIN users u ON p.user_id = u.user_id WHERE u.username = '" + user + "';")
    #cur.execute("SELECT pname FROM project;")
    names = cur.fetchall()
    conn.close()


    return render_template('load_saves.html.jinja' , names = names)

@bp.route('/display_save', methods=['POST'])
def display_save():
    
    return