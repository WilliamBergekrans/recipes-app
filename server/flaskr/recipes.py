from flask import Blueprint, jsonify

bp = Blueprint('recipes', __name__, url_prefix='/recipes')


@bp.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')
