from flask import Blueprint, jsonify, request

from src.main.adapters import request_adapter_no_token, request_adapter
from src.main.composers.usuario import cadastrar_usuario_composer,\
                                     buscar_usuarios_composer,\
                                     buscar_usuario_por_id_composer,\
                                     atualizar_usuario_composer, \
                                     excluir_usuario_composer, \
                                     login_composer

from src.errors import handle_errors

blueprint = Blueprint("usuario_routes", __name__)

@blueprint.route("/usuario/cadastrar", methods=["POST"])
def cadastrar_usuario():
    http_response = None

    try:
        http_response = request_adapter_no_token(request, cadastrar_usuario_composer())
    except Exception as e:
        http_response = handle_errors(e)
    
    return jsonify(http_response.body), http_response.status_code

@blueprint.route("/usuario/login", methods=["POST"])
def login():
    http_response = None

    try:
        http_response = request_adapter_no_token(request, login_composer())
    except Exception as e:
        http_response = handle_errors(e)
    
    return jsonify(http_response.body), http_response.status_code

@blueprint.route("/usuario", methods=["GET"])
def buscar_usuarios():
    http_response = None

    try:
        http_response = request_adapter(request, buscar_usuarios_composer())
    except Exception as e:
        http_response = handle_errors(e)
    
    return jsonify(http_response.body), http_response.status_code