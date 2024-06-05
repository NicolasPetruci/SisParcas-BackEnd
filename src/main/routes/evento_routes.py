from flask import Blueprint, jsonify, request

from src.main.adapters import request_adapter_dono,\
                              request_adapter_adm, \
                              request_adapter

from src.main.composers.tipo_evento import cadastrar_tipo_evento_composer,\
                                     buscar_tipo_eventos_composer,\
                                     buscar_tipo_evento_por_id_composer,\
                                     atualizar_tipo_evento_composer, \
                                     excluir_tipo_evento_composer

from src.main.composers.evento import cadastrar_evento_composer,\
                                     buscar_eventos_composer,\
                                     buscar_evento_por_id_composer,\
                                     atualizar_evento_composer, \
                                     excluir_evento_composer

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

@blueprint.route("/evento/cadastrar", methods=["POST"])
def cadastrar_evento():
    http_response = None

    try:
        http_response = request_adapter_adm(request, cadastrar_evento_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code

@blueprint.route("/evento", methods=["GET"])
def buscar_eventos():
    http_response = None
    try:
        if(request.args):
            http_response = request_adapter_adm(request, buscar_evento_por_id_composer())
        else:
            http_response = request_adapter_adm(request, buscar_eventos_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
        
    return jsonify(http_response.body), http_response.status_code

@blueprint.route("/evento/atualizar", methods=["PUT"])
def atualizar_evento():
    http_response = None

    try:
        http_response = request_adapter_adm(request, atualizar_evento_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code

@blueprint.route("/evento/excluir", methods=["DELETE"])
def excluir_evento():
    http_response = None
    try:
        http_response = request_adapter_adm(request, excluir_evento_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code