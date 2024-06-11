from flask import Blueprint, jsonify, request

from src.main.adapters import request_adapter_dono,\
                              request_adapter_adm, \
                              request_adapter

from src.main.composers.tipo_evento import *

from src.main.composers.evento import *

from flask_cors import cross_origin
from src.errors import handle_errors

blueprint = Blueprint("evento_routes", __name__)

@blueprint.route("/evento/tipo/cadastrar", methods=["POST"])
@cross_origin()
def cadastrar_tipo_evento():
    http_response = None

    try:
        http_response = request_adapter_dono(request, cadastrar_tipo_evento_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code

@blueprint.route("/evento/tipo", methods=["GET"])
@cross_origin()
def buscar_tipo_eventos():
    http_response = None
    try:
        http_response = request_adapter_dono(request, buscar_tipo_eventos_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
        
    return jsonify(http_response.body), http_response.status_code

@blueprint.route("/evento/tipo/excluir", methods=["DELETE"])
@cross_origin()
def excluir_tipo_evento():
    http_response = None
    try:
        http_response = request_adapter_dono(request, excluir_tipo_evento_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code

@blueprint.route("/evento/cadastrar", methods=["POST"])
@cross_origin()
def cadastrar_evento():
    http_response = None

    try:
        http_response = request_adapter_adm(request, cadastrar_evento_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code

@blueprint.route("/evento", methods=["GET"])
@cross_origin()
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
@cross_origin()
def atualizar_evento():
    http_response = None

    try:
        http_response = request_adapter_adm(request, atualizar_evento_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code

@blueprint.route("/evento/excluir", methods=["DELETE"])
@cross_origin()
def excluir_evento():
    http_response = None
    try:
        http_response = request_adapter_adm(request, excluir_evento_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code


@blueprint.route("/evento/inscrever", methods=["PUT"])
@cross_origin()
def inscrever_evento():
    http_response = None
    try:
        http_response = request_adapter(request, inscrever_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code


@blueprint.route("/evento/desinscrever", methods=["PUT"])
@cross_origin()
def desinscrever_evento():
    http_response = None
    try:
        http_response = request_adapter(request, desinscrever_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code

@blueprint.route("/evento/listar-participantes", methods=["GET"])
@cross_origin()
def listar_participantes_evento():
    http_response = None
    try:
        http_response = request_adapter(request, listar_participantes_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code


@blueprint.route("/evento/visualizar-eventos", methods=["GET"])
@cross_origin()
def visualizar_eventos():
    http_response = None
    try:
        http_response = request_adapter(request, visualizar_eventos_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code