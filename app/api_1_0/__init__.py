from flask import Blueprint, request, g, current_app, make_response
import jwt

from app.models.user import User

from app.permission_control.falsk_login_helper import load_token

api = Blueprint('api', __name__)

from . import errors, user, auth


@api.before_request
def before_api_request():
    if request.path == "/api/1.0/tokenauth":
        return None
    
    token = request.cookies.get('jwt')
    try:
        token_payload = jwt.decode(token, current_app.config.get('SECRET_KEY'))
        user_id = token_payload.get("user_id", "")
        user = User.get_user_by_id(user_id)
        if not user:
            response = make_response('User does not exist.')
            response.status_code = 403
            return response
    except jwt.ExpiredSignatureError as e:
        response = make_response('Your JWT has expired')
        response.status_code = 401
        return response
    except jwt.DecodeError as e:
        response = make_response('Your JWT is invalid')
        response.status_code = 401
        return response