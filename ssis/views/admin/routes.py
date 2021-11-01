from flask import request, render_template, redirect
from flask.helpers import url_for
from werkzeug.security import generate_password_hash, check_password_hash
from .utils import verified
from . import admin

@admin.route('/', methods=['GET', 'POST'])
def login() -> str:
    if request.method == 'POST':
        redirect(url_for('homepage'))
    return render_template('index.html')

