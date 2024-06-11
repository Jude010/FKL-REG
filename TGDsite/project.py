from flask import Flask , render_template , Blueprint , request ,session
from TGDsite.db import connect
from TGDsite.resources import readText , projects


bp = Blueprint('project',__name__, url_prefix='/project')

@bp.route('/project_results', methods=['POST'])
def project_results():
    results = request.form
    project = session['project']
    for i in range(project['stair_num']):
        project["stair" + str(i)]['name'] = results[str(i)]
        project["stair" + str(i)]['inside'] = results["internal" + str(i)]
        project["stair" + str(i)]['steps'] = results["steps" + str(i) ]
    return render_template('project_results.html', project = project)