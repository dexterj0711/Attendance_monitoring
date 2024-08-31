from flask import Blueprint, render_template, request, current_app, flash, redirect, url_for


bp = Blueprint('attendance', __name__, template_folder='templates')

@bp.route('/attendance', methods=['GET', 'POST'])
def attendance():
  

    return render_template('attendance.html')
