from flask import Blueprint,render_template,redirect,request,session

bp = Blueprint('adminInstructor',__name__,template_folder='templates')

@bp.route('/adminInstructor')
def adminInstructor():
    return render_template('adminInstructor.html')