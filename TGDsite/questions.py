from flask import Flask , render_template , Blueprint , request ,session
from TGDsite.db import connect
from TGDsite.resources import project_parts, readText


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
    project = project_parts.project(results['name'],'bla', results["stairs"],results['floors'])
    session['projet'] = None
    session['project'] = project.serialize()
    return render_template('domestic.html.jinja' , project = project)

@bp.route('/stairs', methods=['POST'])
def stair_questions():
    results = request.form
    project = session['project']
    project['privacy'] = results['privacy']
    session['project'] = None
    session['project'] = project
    return render_template('stair_questons.html.jinja' , project = project)

@bp.route('/name')
def new_project():# to new project
    return render_template("new_project.html.jinja")

