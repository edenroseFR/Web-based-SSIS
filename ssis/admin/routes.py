from flask import Blueprint, request, render_template, redirect, current_app
from flask.helpers import url_for
from .utils import verified
from . import admin

@admin.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        redirect(url_for('homepage'))
    return render_template('index.html')


@admin.route('/admin/signup')
def signup():
    return render_template('signup.html')


@admin.route('/admin/confirm_identity', methods=['GET', 'POST'])
def confirm_identity():
    username = request.form.get('username')
    password = request.form.get('password')
    password2 = request.form.get('passwordConfirmation')

    if verified(username, password, password2):
        return redirect(url_for('homepage'))
    return render_template('signup.html')