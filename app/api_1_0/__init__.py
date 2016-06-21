from flask import Blueprint, request, g
from app.permission_control.falsk_login_helper import load_token

api = Blueprint('api', __name__)

from . import errors, user


@api.before_request
def before_api_request():
    if request.json is None:
        return errors.bad_request('Invalid JSON in body.')
    token = request.json.get('token')
    if not token:
        return errors.unauthorized('Authentication token not provided.')
    user = load_token(token)
    if not user:
        return errors.unauthorized('Invalid authentication token.')
    g.current_user = user
