from flask import Blueprint, request, g, current_app
import jwt

from app.models.user import User

from app.permission_control.falsk_login_helper import load_token

api = Blueprint('api', __name__)

from . import errors, user, auth


@api.before_request
def before_api_request():
    if request.path == "/api/1.0/tokenauth":
            return None

    if request.json is None:
        return errors.bad_request('Invalid JSON in body.')
    token = request.json.get('token')
    if not token:
        return errors.unauthorized('Authentication token not provided.')

    token_payload = jwt.decode(token, current_app.config.get('SECRET_KEY'))
    user_id = token_payload.get("user_id", "")
    user = User.get_user_by_id(user_id)
    if not user:
        return errors.unauthorized('Invalid authentication token.')
    g.current_user = user
