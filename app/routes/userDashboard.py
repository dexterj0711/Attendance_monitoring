from flask import Flask,Blueprint,redirect,render_template,current_app
import mysql.connector

bp = Blueprint('userDashboard', __name__, template_folder='templates')
@bp.route('/userDashboard')
def userDashboard():
    total_subjects = 42
    total_classrooms = 15

    try:
        conn = current_app.mysql
        cursor = conn.cursor()
        cursor.execute('select * from Subjects')
        subjects = cursor.fetchall()


    except mysql.connector.Error as e:
        return f"Erro: {e}"
    
    return render_template('userDashboard.html', total_subjects=total_subjects, total_classrooms=total_classrooms,subjects = subjects)