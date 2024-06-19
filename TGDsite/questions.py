from flask import Flask , render_template , Blueprint , request ,session
from TGDsite.db import connect
from TGDsite.resources import project_parts, readText


bp = Blueprint('questions',__name__, url_prefix='/questions')

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

@bp.route('/new_project', methods=['POST'])
def stair_questions():
    return render_template('stair_questons.html.jinja' , project = project)

@bp.route('/new_project')
def new_project():# to new project
    return render_template("new_project.html.jinja")

@bp.route('/new_project')
def domestic():# to domestic/non domestic
    results = request.form
    project = project_parts.project(results['name'],None, results["stairs"],results['floors'])
    session['project'] = project.serialize()
    return render_template('domestic.html.jinja' , project = session['project'])