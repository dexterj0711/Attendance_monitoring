from flask import Flask
import mysql.connector
from .config import Config
from .routes.attendance import bp as attendance_bp
from .routes.classroom import bp as classroom_bp
from .routes.subject import bp as subject_pb
from.routes.admin import bp as admin_bp
from .routes.admin_addSubject import bp as adminAddSubject_bp
from .routes.userDashboard import bp as userDashboard_bp
from .routes.roomContent import bp as roomContent_bp
from .routes.adminInstructor import bp as adminInstructor_bp
from .routes.adminAddClassroom import bp as adminAddClassroom_bp


def create_app():
    app = Flask(__name__)
    app.secret_key = 'dexterjaemsdegayo'
    
    # Set default configuration
    app.config.from_object(Config)
    
    # Initialize MySQL connection
    app.mysql = mysql.connector.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DATABASE']
    )
    
    # Register blueprints
    app.register_blueprint(attendance_bp)
    app.register_blueprint(classroom_bp)
    app.register_blueprint(subject_pb)
    app.register_blueprint(admin_bp)
    app.register_blueprint(adminAddSubject_bp)
    app.register_blueprint(userDashboard_bp)
    app.register_blueprint(roomContent_bp)
    app.register_blueprint(adminInstructor_bp)
    app.register_blueprint(adminAddClassroom_bp)
    return app
