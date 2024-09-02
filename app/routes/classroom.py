from flask import Blueprint, render_template, request, redirect, url_for, current_app
import mysql.connector
bp = Blueprint('classroom', __name__, template_folder='templates')

@bp.route('/classrooms')
def classroom():
    try:
        conn = current_app.mysql
        cursor = conn.cursor()
        cursor.execute('select * from Rooms')
        classrooms = cursor.fetchall()

    except mysql.connector.Error as e:
        return f"mysql error: {e}"
  
    return render_template('classroom.html', classrooms = classrooms)
