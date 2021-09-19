from flask import Flask, request, render_template, redirect
from flask.helpers import url_for
from ssis import userFound

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        redirect(url_for('homepage'))
    return render_template('index.html')


@app.route('/homepage', methods=['GET', 'POST'])
def homepage():
    username = request.form.get('username')
    password = request.form.get('password')
    if userFound(username,password):
        return "<h1>Here</h1>"
    else:
        return render_template('index.html')

@app.route('/signup')
def signup():
    return "<h1>Sign Up</h1>"



if __name__ == '__main__':
    app.run(debug=True)