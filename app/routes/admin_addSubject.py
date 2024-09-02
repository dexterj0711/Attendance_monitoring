from flask import Blueprint, render_template, request, redirect, current_app, flash
import mysql.connector

bp = Blueprint('adminAddsubject', __name__, template_folder='templates')

@bp.route('/adminAddSubject', methods=['POST', 'GET'])
def adminAddSubject():
    if request.method == 'POST':
        subject_code = request.form['subject_code']
        subject_name = request.form['subject_name']
        schedule = request.form['schedule']
        time = request.form['time']
        instructor = request.form['instructor']
        status = request.form['status']
        room_id = request.form['room_id']

        try:
            conn = current_app.mysql
            cursor = conn.cursor()

            cursor.execute("""INSERT INTO Subjects (subject_code, subject_name, schedule, time, instructor_id, status, room_id) 
                              VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                           (subject_code, subject_name, schedule, time, instructor, status, room_id))
            conn.commit()

            flash('Subject successfully added!', 'success')
            return redirect('/adminAddSubject') 
            
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            flash(f"Error: {err}", 'error')
            return redirect('/adminAddSubject')
        
        finally:
            if cursor:
                cursor.close()

    try:
        conn = current_app.mysql
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Subjects")
        subjects = cursor.fetchall()
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        subjects = []
    
    finally:
        if cursor:
            cursor.close()
    
    return render_template('adminAddSubject.html', subjects=subjects)
