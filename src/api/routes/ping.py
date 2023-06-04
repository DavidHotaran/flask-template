from flask import Blueprint

ping_api = Blueprint('ping_api', __name__)

@ping_api.route('/ping', methods=['GET'])
def ping():
    return {"message": "pong"}, 200