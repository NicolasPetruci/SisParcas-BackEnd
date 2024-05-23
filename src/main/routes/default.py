from flask import Blueprint, jsonify

blueprint = Blueprint("blueprint_default", __name__)

@blueprint.route("/")
def default():
    return jsonify({"data": "OK"})