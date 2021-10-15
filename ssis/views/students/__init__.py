from flask import Blueprint

student = Blueprint('student', __name__)

from . import routes