from flask import Blueprint, jsonify, request

from src.main.adapters import request_adapter
from src.main.composers.cargo import cadastrar_cargo_composer, buscar_cargos_composer, buscar_cargo_por_id_composer

from src.errors import handle_errors

blueprint = Blueprint("cargo_routes", __name__)

@blueprint.route("/cargo/cadastrar", methods=["POST"])
def cadastrar_cargo():
    http_response = None

    try:
        http_response = request_adapter(request, cadastrar_cargo_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code

@blueprint.route("/cargo", methods=["GET"])
def buscar_cargos():
    http_response = None
    try:
        if(request.args):
            http_response = request_adapter(request, buscar_cargo_por_id_composer())
        else:
            http_response = request_adapter(request, buscar_cargos_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
        
    return jsonify(http_response.body), http_response.status_code