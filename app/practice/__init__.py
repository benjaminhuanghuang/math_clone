from flask import Blueprint

practice = Blueprint('practice', __name__)

from . import routes

