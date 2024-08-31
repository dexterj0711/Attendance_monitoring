from flask import Blueprint,render_template,current_app
import mysql.connector

bp = Blueprint('subject', __name__, template_folder='templates')
@bp.route('/subject')
def subject():
    try:
        conn = current_app.mysql
        cursor = conn.cursor()
        cursor.execute('select * from Subjects')
        subjects = cursor.fetchall()
    except mysql.connector.Error as e:
        return f"mysql error: {e}"
    return render_template('subjects.html', subjects = subjects)