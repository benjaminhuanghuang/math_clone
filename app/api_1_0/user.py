from flask import jsonify
from flask_login import current_user
from . import api


@api.route('/privatehello', methods=['GET'])
def private_hello():
    return jsonify("private hello" + current_user.username)

@api.route('/getuserlist', methods=['GET'])
def get_user_list():
    return jsonify({'status': 'ok'})

@api.route('/getuserinfo/<user_name>', methods=['GET'])
def get_user_info():

    return jsonify({'status': 'ok'})

@api.route('/updateuserinfo/<user_name>', methods=['PUT'])
def update_user_info():

    return jsonify({'status': 'ok'})
