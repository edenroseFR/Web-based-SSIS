from flask import request, render_template, redirect
from flask.helpers import url_for
from werkzeug.security import generate_password_hash, check_password_hash
from ...models.student import Student
from ...models.course import Course
from ...models.college import College
from . import admin
from .utils import admin_found

@admin.route('/')
def login() -> str:
    return render_template('index.html')


@admin.route('/login', methods = ['POST'])
def verify() -> str:
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(username,password)
        if admin_found(username, password):
            students = Student().get_all(1,5)
            courses = Course().get_all(paginate=False)
            colleges = College().get_all(paginate=False)
            return render_template('students.html', 
                                    data = [students,courses,colleges],
                                    datacount = f'{len(students)} Students')
    return redirect(url_for('admin.login'))
