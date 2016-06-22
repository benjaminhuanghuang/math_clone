from flask import Blueprint

api_public = Blueprint('api_public', __name__)

from . import routes
