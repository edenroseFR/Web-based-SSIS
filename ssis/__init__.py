from flask import Flask


def create_app():
    app = Flask(__name__)

    # import blueprints
    from .admin import admin
    from .students import student
    from .courses import course
    from .colleges import college

    # register blueprints
    app.register_blueprint(admin)
    app.register_blueprint(student)
    app.register_blueprint(course)
    app.register_blueprint(college)

    return app