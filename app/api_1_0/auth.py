from flask import current_app, request
from flask_login import login_user
import jsonpickle
from . import api
import jwt
from flask import make_response
from datetime import datetime, timedelta

from app.models.user import User


@api.route('/tokenauth', methods=['POST'])
def token_auth():
    parameter = jsonpickle.decode(request.data)
    user = User.get_user_by_name(parameter.get("username", ""))
    if user and User.verify_password(user, parameter.get("password", "")):
        user_obj = User(user)
        login_user(user_obj)  # put user into session

    token_payload = {'user_name': user_obj.username,
                     'user_id':user_obj.id,
                     'role': user_obj.role,
                     'utc_exp': datetime.utcnow() + timedelta(minutes=current_app.config.get('COOKIE_DURATION', 60)),
                     'utc_now': datetime.utcnow()}

    token = jwt.encode(token_payload, current_app.config.get('SECRET_KEY', 'secret'))
    response = make_response(token)
    response.set_cookie('jwt', token)
    return response
