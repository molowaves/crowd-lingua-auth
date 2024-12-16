from flask import Blueprint, jsonify


api_view = Blueprint('api_view', __name__)


@api_view.route('/')
def index():
    return jsonify(data='data')