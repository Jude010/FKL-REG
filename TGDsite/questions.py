from flask import Flask , render_template , Blueprint , request
from TGDsite.db import connect
from TGDsite.resources import readText


bp = Blueprint('questions',__name__, url_prefix='/questions')

@bp.route('/')
def index():
    conn = connect.get_db_conn()
    cur = conn.cursor()
    cur.execute('SELECT guide_name FROM guide;')
    guides = cur.fetchall()
    return render_template('questions.html', guides=guides)
    
@bp.route('/guides', methods=['GET'])
def guides():
    guides = request.args
    #text = readText.readText(guides)
    return render_template('guides.html' , guides= guides)