from flask import redirect , render_template , Blueprint , request ,session , url_for
from TGDsite.db import connect
from TGDsite.resources import project_parts, readText , tools


bp = Blueprint('project',__name__, url_prefix='/project')

@bp.route('/project_results', methods=['POST'])
def project_results():
    results = request.form
    project = session['project']
    for i in range(project['stair_num']):
        project["stair" + str(i)]['name'] = results[str(i)]
        project["stair" + str(i)]['inside'] = results["internal" + str(i)]
        project["stair" + str(i)]['rise'] = results["rise" + str(i) ]
        if "part_m" + str(i) in results.keys():
            project["stair" + str(i)]['part_m'] = True
        else:
            project["stair" + str(i)]['part_m'] = False

        project["stair" + str(i)]['min_f'] = tools.calc_flights(project["stair" + str(i)],project["privacy"])
    return render_template('project_results.html.jinja', project = project)

@bp.route("/save_project")
def save_project():
    conn = connect.get_db_conn()
    cur = conn.cursor()
    project = session['project']
    user = session['user']

    #insert the project info from session into the DB
    p_id = cur.execute("INSERT INTO project (p_name , floors,  privacy) VALUES ('" 
                + str(project['name']) + "', '"
                + str(project['floors']) + "', '"
                + str(project['privacy']) + "') RETURNING proj_id;")
    
    #insert the stairs info from session into the DB and associate with the project
    for stair in project['stairs']:
        s_id = cur.execute("INSERT INTO stairs (s_name, rise, internal , part_m) VALUES ('"
                    + str(stair['name']) + "', '"
                    + str(stair['rise']) + "', '"
                    + str(stair['inside']) + "', '"
                    + str(stair['part_m']) 
                    + "') RETURNING stair_id;")
        
        cur.execute("INSERT INTO proj_stair (stair_id , proj_id) VALUES ('"
                     + s_id[0] +"','" + p_id[0] + "');")
        
    u_id = cur.execute("SELECT user_id FROM users WHERE users.username LIKE '" + user + "';")
    
    cur.execute("INSERT INTO saves (user_id , proj_id) VALUES '" + u_id[0] + "', '" + p_id[0] + "';")

    return redirect(url_for('project.display'))

@bp.route("/display")
def display():
    return None



