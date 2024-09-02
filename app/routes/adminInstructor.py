from flask import Blueprint,render_template,redirect,request,session,current_app
import mysql.connector

bp = Blueprint('adminInstructor',__name__,template_folder='templates')

@bp.route('/adminInstructor', methods = ['POST','GET'])
def adminInstructor():

    if request.method == 'POST':
        instructor_id= request.form['USN']
        instructor_name = request.form['instructor_name']
        department = request.form['department']
        profile_picture = request.form['profile_picture']

        try:
            conn = current_app.mysql
            cursor = conn.cursor()
            cursor.execute('insert into instructor(instructor_id,instructor_name,department,profile_picture) Values(%s,%s,%s,%s)',(instructor_id,instructor_name,department,profile_picture))
            conn.commit()
            return redirect('/adminInstructor')
        except mysql.connector.Error as e:
            return f"error: {e}"
    return render_template('adminInstructor.html')