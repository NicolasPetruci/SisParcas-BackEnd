from flask import Blueprint, jsonify, request

from src.main.adapters import request_adapter_dono,\
                              request_adapter_adm, \
                              request_adapter, \
                              request_adapter_mestre

from src.main.composers.genero import cadastrar_genero_composer,\
                                     buscar_generos_composer,\
                                     buscar_genero_por_id_composer,\
                                     atualizar_genero_composer, \
                                     excluir_genero_composer

from src.main.composers.rpg import *

from src.main.composers.mestre import cadastrar_mestre_composer,\
                                        buscar_mestres_composer, \
                                        atualizar_mestre_composer, \
                                        buscar_mestre_por_id_composer, \
                                        excluir_mestre_composer, \
                                        deferir_mestre_composer, \
                                        indeferir_mestre_composer

from src.main.composers.sessao import cadastrar_sessao_composer,\
                                     buscar_sessoes_composer,\
                                     buscar_sessao_por_id_composer,\
                                     atualizar_sessao_composer, \
                                     excluir_sessao_composer

from flask_cors import cross_origin
from src.errors import handle_errors

blueprint = Blueprint("rpg_routes", __name__)



@blueprint.route("/rpg/mestre/deferir", methods=["PUT"])
@cross_origin()
def deferir_mestre():
    http_response = None

    try:
        http_response = request_adapter(request, deferir_mestre_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code

@blueprint.route("/rpg/mestre/indeferir", methods=["PUT"])
@cross_origin()
def indeferir_mestre():
    http_response = None

    try:
        http_response = request_adapter(request, indeferir_mestre_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code

@blueprint.route("/rpg/mestre/cadastrar", methods=["POST"])
@cross_origin()
def cadastrar_mestre():
    http_response = None

    try:
        http_response = request_adapter(request, cadastrar_mestre_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code

@blueprint.route("/rpg/mestre", methods=["GET"])
@cross_origin()
def buscar_mestres():
    http_response = None
    try:
        if(request.args):
            http_response = request_adapter(request, buscar_mestre_por_id_composer())
        else:
            http_response = request_adapter(request, buscar_mestres_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
        
    return jsonify(http_response.body), http_response.status_code

@blueprint.route("/rpg/mestre/excluir", methods=["DELETE"])
@cross_origin()
def excluir_mestre():
    http_response = None
    try:
        http_response = request_adapter_dono(request, excluir_mestre_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code

@blueprint.route("/rpg/genero/cadastrar", methods=["POST"])
@cross_origin()
def cadastrar_genero():
    http_response = None

    try:
        http_response = request_adapter_mestre(request, cadastrar_genero_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code

@blueprint.route("/rpg/genero", methods=["GET"])
@cross_origin()
def buscar_generos():
    http_response = None
    try:
        http_response = request_adapter_mestre(request, buscar_generos_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
        
    return jsonify(http_response.body), http_response.status_code

@blueprint.route("/rpg/genero/excluir", methods=["DELETE"])
@cross_origin()
def excluir_genero():
    http_response = None
    try:
        http_response = request_adapter_mestre(request, excluir_genero_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code

@blueprint.route("/rpg/cadastrar", methods=["POST"])
@cross_origin()
def cadastrar_rpg():
    http_response = None

    try:
        http_response = request_adapter(request, cadastrar_rpg_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code

@blueprint.route("/rpg", methods=["GET"])
@cross_origin()
def buscar_rpgs():
    http_response = None
    try:
        if(request.args):
            http_response = request_adapter(request, buscar_rpg_por_id_composer())
        else:
            http_response = request_adapter(request, buscar_rpgs_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
        
    return jsonify(http_response.body), http_response.status_code

@blueprint.route("/rpg/atualizar", methods=["PUT"])
@cross_origin()
def atualizar_rpg():
    http_response = None

    try:
        http_response = request_adapter_mestre(request, atualizar_rpg_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code

@blueprint.route("/rpg/excluir", methods=["DELETE"])
@cross_origin()
def excluir_rpg():
    http_response = None
    try:
        http_response = request_adapter_dono(request, excluir_rpg_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code


@blueprint.route("/rpg/inscrever", methods=["PUT"])
@cross_origin()
def inscrever_rpg():
    http_response = None
    try:
        http_response = request_adapter(request, inscrever_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code


@blueprint.route("/rpg/desinscrever", methods=["PUT"])
@cross_origin()
def desinscrever_rpg():
    http_response = None
    try:
        http_response = request_adapter(request, desinscrever_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code 

@blueprint.route("/rpg/sessao/cadastrar", methods=["POST"])
@cross_origin()
def cadastrar_sessao():
    http_response = None

    try:
        http_response = request_adapter(request, cadastrar_sessao_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code

@blueprint.route("/rpg/sessao", methods=["GET"])
@cross_origin()
def buscar_sessoes():
    http_response = None
    try:
        if(request.args):
            http_response = request_adapter(request, buscar_sessao_por_id_composer())
        else:
            http_response = request_adapter(request, buscar_sessoes_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
        
    return jsonify(http_response.body), http_response.status_code

@blueprint.route("/rpg/sessao/atualizar", methods=["PUT"])
@cross_origin()
def atualizar_sessao():
    http_response = None

    try:
        http_response = request_adapter_mestre(request, atualizar_sessao_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code

@blueprint.route("/rpg/sessao/excluir", methods=["DELETE"])
@cross_origin()
def excluir_sessao():
    http_response = None
    try:
        http_response = request_adapter_dono(request, excluir_sessao_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code   

@blueprint.route("/rpg/listar-jogadores", methods=["GET"])
@cross_origin()
def listar_jogadores_rpg():
    http_response = None
    try:
        http_response = request_adapter(request, listar_jogadores_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code


@blueprint.route("/rpg/visualizar-rpgs", methods=["GET"])
@cross_origin()
def visualizar_rpgs():
    http_response = None
    try:
        http_response = request_adapter(request, visualizar_rpgs_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code