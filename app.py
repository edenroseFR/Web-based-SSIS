from config import app
from ssis.admin.routes import admin
from ssis.students.routes import student
from ssis.courses.routes import course
from ssis.colleges.routes import college

app.register_blueprint(admin, url_prefix='/ssis')
app.register_blueprint(student, url_prefix='/students')
app.register_blueprint(course, url_prefix='/courses')
app.register_blueprint(college, url_prefix='/colleges')


if __name__ == '__main__':
    app.run(debug=True)