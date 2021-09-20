from flask import Flask, request, render_template, redirect
from flask.helpers import url_for
from SSIShelper import userFound, verified

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

    if userFound(username,password):
        return render_template('homepage.html')
    else:
        return render_template('index.html')


@app.route('/confirm_identity', methods=['GET', 'POST'])
def confirm_identity():
    username = request.form.get('username')
    password = request.form.get('password')
    password2 = request.form.get('passwordConfirmation')

    if verified(username, password, password2):
        return render_template('homepage.html')
    return render_template('signup.html')



if __name__ == '__main__':
    app.run(debug=True)