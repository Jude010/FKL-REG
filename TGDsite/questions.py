from flask import Flask , render_template , Blueprint , request ,session , redirect , url_for
from TGDsite.db import connect
from TGDsite.resources import project_parts, readText , tools


bp = Blueprint('questions',__name__, url_prefix='/new_project')

@bp.route('/guide_index')
def guide_index():
    conn = connect.get_db_conn()
    cur = conn.cursor()
    cur.execute('SELECT guide_name FROM guide;')
    names = cur.fetchall()
    conn.close()
    return render_template('guide_index.html.jinja', names=names)
    
@bp.route('/guides', methods=['GET'])
def guides():
    guides = [] 
    guides = request.args.keys()
    text = readText.readText(guides)
    return render_template('guides.html.jinja' , text = text)

@bp.route('/domestic', methods=['POST'])
def domestic():# to domestic/non domestic
    results = request.form
    project = project_parts.project(results['name'],'bla', results["stairs"],results['floors'], results['ramps'])
    session['projet'] = None
    session['project'] = project.serialize()
    return render_template('domestic.html.jinja' , project = project)

@bp.route('/stairs', methods=['POST'])
def stair_questions_1():
    results = request.form
    project = session['project']
    project['privacy'] = results['privacy']
    session['project'] = None
    session['project'] = project
    if project['stair_num'] > 0:
        return render_template('stair_questons.html.jinja' , project = project)
    else :
        return redirect(url_for('.ramp_questions' , code=307))

@bp.route('/ramps', methods=['POST'])
def ramp_questions():
    results = request.form
    project = session['project']
    for i in range(project['stair_num']):
        for j in range( int(project['stairs'][str(i)]['floors'])):
            rise = results[str(i) + str(j) + 'rise']
            privacy = project['privacy']
            part_m = project['stairs'][str(i)]['part_m']
            inside = project['stairs'][str(i)]['inside'] 
            temp = {}
            project['stairs'][str(i)]['floor' + str(j)] = {'rise': rise}
            project['stairs'][str(i)]['floor' + str(j)]['flights'] = tools.calc_flights(rise , privacy , part_m , inside)


    session['project'] = None
    session['project'] = project
    
    return render_template('ramp_questions.html.jinja' , project=project ) 

@bp.route('/')
def new_project():# to new project
    return render_template("new_project.html.jinja")

@bp.route('/stairs2', methods=['POST'])
def stair_questions_2():
    results = request.form
    project = session['project']
    for i in range(project['stair_num']):
        project['stairs'][str(i)]['name'] = results[str(i)]
        project['stairs'][str(i)]['inside'] = results["internal" + str(i)]
        project['stairs'][str(i)]['floors'] = results["floors" + str(i)]
        if "part_m" + str(i) in results.keys():
            project['stairs'][str(i)]['part_m'] = True
        else:
            project['stairs'][str(i)]['part_m'] = False
    
    session['project'] = None
    session['project'] = project   

    return render_template("stair_questions_2.html.jinja" , project = project)


