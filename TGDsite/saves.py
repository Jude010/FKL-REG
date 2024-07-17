from flask import Blueprint ,render_template , session , request
from TGDsite.db import connect 

bp = Blueprint('saves' , __name__ , url_prefix='/saves')

@bp.route('/load_saves')
def load_saves():
    user = session['user']
    conn = connect.get_db_conn()
    cur = conn.cursor()

    # fetch all project names associated with current user
    cur.execute("SELECT pname , proj_id FROM project p INNER JOIN users u ON p.user_id = u.user_id WHERE u.username = '" + user + "';")
    #cur.execute("SELECT pname FROM project;")
    names = cur.fetchall()
    conn.close()


    return render_template('load_saves.html.jinja' , names = names)

@bp.route('/display_save', methods=['POST'])
def display_save():
    results = request.form
    user = session['user']
    conn = connect.get_db_conn()
    cur = conn.cursor()

    #fetch all project details using project id from POST
    cur.execute("SELECT pname ,floors ,privacy FROM project p WHERE proj_id = '" + request['id'] + "';" )
    proj = cur.fetchall()

    cur.execute("SELECT stair_id WHERE proj_id = '" + request['id'] + "';" )


    return render_template('load_project.html.jinja')