from flask import jsonify, g
from . import api
from .errors import forbidden, bad_request
from app.models.user import User

@api.route('/hello', methods=['GET'])
def hello():
    return jsonify({'status': 'ok'})

@api.route('/getuserlist', methods=['GET'])
def get_user_list():
    return jsonify({'status': 'ok'})

@api.route('/getuserinfo/<user_name>', methods=['GET'])
def get_user_info():

    return jsonify({'status': 'ok'})

@api.route('/updateuserinfo/<user_name>', methods=['PUT'])
def update_user_info():

    return jsonify({'status': 'ok'})
