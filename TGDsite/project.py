from flask import redirect , render_template , Blueprint , request ,session , url_for
from TGDsite.db import save
from TGDsite.resources import project_parts, readText , tools
import datetime


bp = Blueprint('project',__name__, url_prefix='/project')

@bp.route('/project_results', methods=['POST'])
def project_results():
    results = request.form
    project = session['project']
    date = datetime.date.today()
    for i in range(project['stair_num']):
        project['stairs'][str(i)]['name'] = results[str(i)]
        project['stairs'][str(i)]['inside'] = results["internal" + str(i)]
        project['stairs'][str(i)]['rise'] = results["rise" + str(i) ]
        if "part_m" + str(i) in results.keys():
            project['stairs'][str(i)]['part_m'] = True
        else:
            project['stairs'][str(i)]['part_m'] = False

        project['stairs'][str(i)]['min_f'] = tools.calc_flights(project['stairs'][str(i)],project["privacy"])
    return render_template('project_results.html.jinja', project = project , date=date)

@bp.route("/save_project", methods=['POST'])
def save_project():
    results = request.form
    save.save_to_db(session['project'],session['user'],results['signature'],results['date'])

    return redirect(url_for('project.project_results'))





