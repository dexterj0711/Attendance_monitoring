from flask import Blueprint,render_template,redirect,request,current_app
import mysql.connector

bp = Blueprint('adminAddClassroom',__name__,template_folder='templates')

@bp.route('/adminAddClassroom',methods = ['POST', 'GET'])
def adminAddClassroom():

    if request.method == 'POST':
        room_number = request.form['roomNumber']
        room_name = request.form['classroomName']

        try: 
            conn = current_app.mysql
            cursor = conn.cursor()
            cursor.execute('insert into Rooms(room_number,room_name) Values(%s,%s)',(room_number,room_name))
            conn.commit()
            return redirect('/adminAddClassroom')
        
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return render_template('error.html', error=str(err))

        finally:
            if cursor:
                cursor.close()
            
    try:
        conn = current_app.mysql
        cursor = conn.cursor()
        cursor.execute('select * from Rooms')
        classrooms = cursor.fetchall()

    except mysql.connector.Error as err:
            print(f"Error: {err}")   
            classrooms = []

    finally:
            if cursor:
                cursor.close()

    return render_template('adminClassroom.html', classrooms = classrooms)