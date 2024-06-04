from flask import Blueprint, jsonify, request

from src.main.adapters import request_adapter_dono
from src.main.composers.tipo_evento import cadastrar_tipo_evento_composer,\
                                     buscar_tipo_eventos_composer,\
                                     buscar_tipo_evento_por_id_composer,\
                                     atualizar_tipo_evento_composer, \
                                     excluir_tipo_evento_composer

from src.errors import handle_errors

blueprint = Blueprint("evento_routes", __name__)

@blueprint.route("/evento/tipo/cadastrar", methods=["POST"])
def cadastrar_tipo_evento():
    http_response = None

    try:
        http_response = request_adapter_dono(request, cadastrar_tipo_evento_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code

@blueprint.route("/evento/tipo", methods=["GET"])
def buscar_tipo_eventos():
    http_response = None
    try:
        http_response = request_adapter_dono(request, buscar_tipo_eventos_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
        
    return jsonify(http_response.body), http_response.status_code

@blueprint.route("/evento/tipo/excluir", methods=["DELETE"])
def excluir_tipo_evento():
    http_response = None
    try:
        http_response = request_adapter_dono(request, excluir_tipo_evento_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code