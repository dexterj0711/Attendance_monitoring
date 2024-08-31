from flask import Blueprint,render_template,redirect

bp = Blueprint('classroomContent',__name__,template_folder='templates') 

@bp.route('/classroomContent')
def classroomContent():
    return render_template('roomContent.html')