from flask import Blueprint, jsonify, request

from src.main.adapters import request_adapter_no_token, request_adapter
from src.main.composers.usuario import *
from flask_cors import cross_origin
from src.errors import handle_errors

blueprint = Blueprint("usuario_routes", __name__)

@blueprint.route("/usuario/cadastrar", methods=["POST"])
@cross_origin()
def cadastrar_usuario():
    http_response = None

    try:
        http_response = request_adapter_no_token(request, cadastrar_usuario_composer())
    except Exception as e:
        http_response = handle_errors(e)
    
    return jsonify(http_response.body), http_response.status_code

@blueprint.route("/usuario/login", methods=["POST", "GET"])
@cross_origin()
def login():
    http_response = None

    try:
        if request.method == "POST":
            http_response = request_adapter_no_token(request, login_composer())
        elif request.method == "GET":
            http_response = request_adapter(request, buscar_usuario_logado_composer())
    except Exception as e:
        http_response = handle_errors(e)
    
    return jsonify(http_response.body), http_response.status_code


@blueprint.route("/usuario", methods=["GET"])
@cross_origin()
def buscar_usuarios():
    http_response = None

    try:
        http_response = request_adapter(request, buscar_usuarios_composer())
    except Exception as e:
        http_response = handle_errors(e)
    
    return jsonify(http_response.body), http_response.status_code

blueprint.route("/usuario/atualizar", methods=["PUT"])
@cross_origin()
def atualizar_usuario():
    http_response = None

    try:
        http_response = request_adapter_dono(request, atualizar_usuario_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code

blueprint.route("/usuario/excluir", methods=["DELETE"])
@cross_origin()
def excluir_usuario():
    http_response = None

    try:
        http_response = request_adapter_dono(request, excluir_usuario_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code

@blueprint.route("/usuario/cargos", methods=["GET"])
@cross_origin()
def buscar_cargos_usuario():
    http_response = None

    try:
        http_response = request_adapter(request, buscar_cargos_usuario_composer())
    except Exception as e:
        http_response = handle_errors(e)
    
    return jsonify(http_response.body), http_response.status_code