from flask import Blueprint

college = Blueprint('college', __name__)

from . import routes