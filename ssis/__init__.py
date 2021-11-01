from flask import Flask
import os

def create_app() -> object:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

    # import blueprints
    from .views.admin import admin
    from .views.students import student
    from .views.courses import course
    from .views.colleges import college

    # register blueprints
    app.register_blueprint(admin)
    app.register_blueprint(student)
    app.register_blueprint(course)
    app.register_blueprint(college)

    return app
