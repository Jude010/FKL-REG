from flask import Blueprint ,render_template , session , request
from TGDsite.db import connect 
from TGDsite.db import save

bp = Blueprint('saves' , __name__ , url_prefix='/saves')

@bp.route('/load_saves')
def load_saves():
    user = session['user']
    conn = connect.get_db_conn()
    cur = conn.cursor()

    # fetch all project names associated with current user
    cur.execute("SELECT pname , proj_id FROM project p INNER JOIN users u ON p.user_id = u.user_id WHERE u.username = '" + user + "';")
    #cur.execute("SELECT pname , proj_id FROM project;")
    names = cur.fetchall()
    conn.close()


    return render_template('load_saves.html.jinja' , names = names)

@bp.route('/display_save', methods=['POST'])
def display_save():
    results = request.form
    user = session['user']
    conn = connect.get_db_conn()
    cur = conn.cursor()
    project= {}

    #fetch all project details using project id from POST
    cur.execute("SELECT pname ,floors ,privacy FROM project p WHERE proj_id = '" + str(results['id']) + "';" )
    proj = cur.fetchall()

    #insert project details into a dict
    project['name'] = proj[0][0]
    project['floors'] = proj[0][1]
    project['privacy'] = proj[0][2]

    #fetch all stair id from db associated with project
    cur.execute("SELECT stair_id FROM proj_stair WHERE proj_id = '" + str(results['id']) + "';" )
    stairs = cur.fetchall()

    count = 0
    t_stairs = {}
    for i in stairs :
        cur.execute("SELECT name , rise, part_m , inside FROM stairs WHERE  stair_id = '" + str(i[0]) +  "';")
        st = cur.fetchall()
        print(st)
        stair = { "name":st[0][0] ,
                  "rise":st[0][1] ,
                  "part_m":st[0][2] ,
                  "inside":st[0][3]}
        
        
        t_stairs[str(count)] = stair

        count += 1

    project['stairs'] = t_stairs
    project['stair_num'] = count

    return render_template('load_project.html.jinja' , project=project)

@bp.route("/save_project", methods=['POST'])
def save_project():
    results = request.form
    project = session['project']
    save.save_to_db(project ,session['user'],results['signature'],results['date'])

    return render_template('load_project.html.jinja' , project = session['project'])
