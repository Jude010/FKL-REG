from flask import redirect , render_template , Blueprint , request ,session , url_for

from TGDsite.resources import project_parts, readText , tools
import datetime


bp = Blueprint('project',__name__, url_prefix='/project')

@bp.route('/project_results', methods=['POST'])
def project_results():
    results = request.form
    project = session['project']
    date = datetime.date.today()
    for i in range(project['ramp_num']):
        project['ramps'][str(i)]['name'] = results[str(i)]
        project['ramps'][str(i)]['inside'] = results["internal" + str(i)]
        project['ramps'][str(i)]['rise'] = results["rise" + str(i)]
        project['ramps'][str(i)]['width'] = results["width" + str(i)]
        if "part_m" + str(i) in results.keys():
            project['ramps'][str(i)]['part_m'] = True
        else:
            project['ramps'][str(i)]['part_m'] = False

        print(str(project['ramps'][str(i)]['rise']) + "test")
        temp = tools.calc_slope(project['ramps'][str(i)]['rise'], project['ramps'][str(i)]['part_m'] ,project["privacy"])
        project['ramps'][str(i)]['going'] = temp[0]
        project['ramps'][str(i)]['slope'] = temp[1]
        temp = None

    session['project'] = None
    session['project'] = project
    print(project)
    return render_template('validation.html.jinja', project = project , date = date)

@bp.route('/validation' , methods=['POST'])
def project_valid():
    results = request.form
    project = session['project']

    print(results)

    project = tools.validate_project(project , results)

    print('/n/n')
    print(results)

    session['project'] = None
    session['project'] = project

    return render_template('project_results.html.jinja', project = project) 