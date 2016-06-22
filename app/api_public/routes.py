from flask import jsonify
from . import api_public


@api_public.route('/hello', methods=['GET'])
def hello():
    return jsonify("Hello")

