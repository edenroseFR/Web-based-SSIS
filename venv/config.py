from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'piesXfrenchwatermelon'
app.config['UPLOAD_PATH'] = 'static/entity_photos/students/'