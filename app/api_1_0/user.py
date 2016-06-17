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
#
# @api.route('/statements/deposit', methods=['POST'])
# def deposit():
#     if not g.current_user.role > 0:
#         return forbidden('You cannot use this API.')
#
#     return jsonify({'status': 'ok'})
#
#
# @api.route('/statements/withdraw', methods=['POST'])
# def withdraw():
#     if not g.current_user.role > 0:
#         return forbidden('You cannot use this API.')
#     return jsonify({'status': 'ok'})
#
#
# @api.route('/admin/listuser', methods=['POST'])
# def list_user():
#     if not g.current_user.role > 0:
#         return forbidden('You cannot use this API.')
#     return jsonify({'status': 'ok'})
