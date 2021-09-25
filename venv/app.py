from models.college import College
from flask import Flask, request, render_template, redirect, flash
from flask.helpers import url_for
from SSIShelper import (
    userFound,
    verified,
    allStudent,
    allCourse,
    allCollege,
    searchStudent,
    addStudent,
    getStudent,
    updateStudent,
    deleteStudent,
    addCourse,
    searchCourse,
    deleteCourse)

app = Flask(__name__)
app.secret_key = 'super_secret_key'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        redirect(url_for('homepage'))
    return render_template('index.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/homepage', methods=['GET', 'POST'])
@app.route('/students', methods=['GET', 'POST'])
def homepage():
    username = request.form.get('username')
    password = request.form.get('password')
    students = allStudent()
    courses = allCourse()
    colleges = allCollege()

    if request.method == 'POST ':
        if userFound(username,password):
            
            return render_template('students.html', data = [students,courses,colleges])
        else:
            return render_template('index.html')
    else:
        return render_template('students.html', data = [students,courses,colleges])


@app.route('/confirm_identity', methods=['GET', 'POST'])
def confirm_identity():
    username = request.form.get('username')
    password = request.form.get('password')
    password2 = request.form.get('passwordConfirmation')

    if verified(username, password, password2):
        return render_template('students.html')
    return render_template('signup.html')


@app.route('/student-search', methods=['GET', 'POST'])
def studentSearch():
    user_input = request.form.get('user-input')
    result = searchStudent(user_input)
    if len(result) != 0:
        return render_template('students.html', data=[result])
    else:
        return redirect(url_for('homepage'))

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    students = allStudent()
    courses = allCourse()
    colleges = allCollege()
    if request.method == 'POST':
        student = {
            'id': request.form.get('student-id'),
            'firstname': request.form.get('firstname'),
            'middlename': request.form.get('middlename'),
            'lastname': request.form.get('lastname'),
            'gender': request.form.get('gender'),
            'yearlevel': request.form.get('yearlevel'),
            'course': request.form.get('course')
        }
        addStudent(student)
        flash(f'{student["firstname"]} added succesfully!', 'info')
        return redirect(url_for('homepage'))
    else:
        return redirect(url_for('homepage'))


@app.route('/update_student/<string:id>', methods=['GET', 'POST'])
def update_student(id):
    data = getStudent(id)
    if request.method == 'POST':
        student = {
            'id': id,
            'firstname': request.form.get('firstname'),
            'middlename': request.form.get('middlename'),
            'lastname': request.form.get('lastname'),
            'gender': request.form.get('gender'),
            'yearlevel': request.form.get('yearlevel'),
            'course': request.form.get('course')
        }
        updateStudent(student)
        flash(f"{student['firstname']}'s data has been changed succesfully!", 'info')
        return redirect(url_for('homepage'))
    else:
        return redirect(url_for('homepage'))


@app.route('/delete_student/<string:id>')
def delete_student(id):
    data = getStudent(id)
    deleteStudent(id)
    flash(f'{data[0]} deleted from the database.', 'info')
    return redirect(url_for('homepage'))


# Courses routes
@app.route('/courses')
def courses():
    students = allStudent()
    courses = allCourse()
    colleges = allCollege()
    return render_template('courses.html', data=[students,courses,colleges])


@app.route('/add_course', methods=['GET', 'POST'])
def add_course():
    courses = allCourse()
    colleges = allCollege()
    if request.method == 'POST':
        course = {
            'code': request.form.get('course-code'),
            'name': request.form.get('course-name'),
            'college': request.form.get('course-college')
        }
        addCourse(course)
        flash(f'{course["code"]} added succesfully!', 'info')
        return redirect(url_for('courses'))
    else:
        return redirect(url_for('courses'))

@app.route('/course-search', methods=['GET', 'POST'])
def courseSearch():
    user_input = request.form.get('user-input')
    result = searchCourse(user_input)
    if len(result) != 0:
        return render_template('courses.html', data=['', result])
    else:
        return redirect(url_for('courses'))


@app.route('/delete_course/<string:id>')
def delete_course(id):
    deleteCourse(id)
    flash(f'{id} deleted from the database.', 'info')
    return redirect(url_for('courses'))

if __name__ == '__main__':
    app.run(debug=True)