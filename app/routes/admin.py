from flask  import Flask,render_template,redirect,Blueprint

bp = Blueprint('admin', __name__, template_folder='templates')

@bp.route('/admin')
def admin():
    return render_template('adminBase.html')