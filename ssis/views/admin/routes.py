from flask import request, render_template, redirect
from flask.helpers import url_for
from . import admin
from .utils import admin_found

@admin.route('/')
def login() -> str:
    return render_template('/admin/login.html')


@admin.route('/login', methods = ['POST'])
def verify() -> str:
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if admin_found(username, password):
            return redirect(url_for('student.students'))
    return redirect(url_for('admin.login'))
