from models.college import College
from flask import Flask, request, render_template, redirect
from flask.helpers import url_for
from SSIShelper import (
    userFound,
    verified,
    allStudent,
    allCourse,
    allCollege,
    searchStudent,
    addStudent)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        redirect(url_for('homepage'))
    return render_template('index.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/homepage', methods=['GET', 'POST'])
def homepage():
    username = request.form.get('username')
    password = request.form.get('password')
    students = allStudent()
    courses = allCourse()
    colleges = allCollege()

    if request.method == 'POST ':
        if userFound(username,password):
            
            return render_template('homepage.html', data = [students,courses,colleges])
        else:
            return render_template('index.html')
    else:
        return render_template('homepage.html', data = [students,courses,colleges])


@app.route('/confirm_identity', methods=['GET', 'POST'])
def confirm_identity():
    username = request.form.get('username')
    password = request.form.get('password')
    password2 = request.form.get('passwordConfirmation')

    if verified(username, password, password2):
        return render_template('homepage.html')
    return render_template('signup.html')


@app.route('/studentSearch', methods=['GET', 'POST'])
def studentSearch():
    user_input = request.form.get('user-input')
    result = searchStudent(user_input)
    if len(result) != 0:
        return render_template('homepage.html', data=[result])
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
        return redirect(url_for('homepage'))
    else:
        return redirect(url_for('homepage'))



if __name__ == '__main__':
    app.run(debug=True)