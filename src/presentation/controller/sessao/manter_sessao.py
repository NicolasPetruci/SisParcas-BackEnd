from src.domain.use_cases.sessao import ManterSessaoInterface
from src.domain.models import Sessao, RPG, Usuario
from src.presentation.http_types import HttpRequest, HttpResponse

class ManterSessaoController():

    @classmethod
    def __init__(self, use_case: ManterSessaoInterface):
        self.__use_case = use_case
    
    @classmethod
    def buscar(self, request: HttpRequest) -> HttpResponse: 
        response = self.__use_case.buscar_sessaos()
        return HttpResponse(
            status_code=200,
            body = response
        )

    @classmethod
    def cadastrar(self, request: HttpRequest) -> HttpResponse:

        form = Sessao(
            0,
            request.body["nome"], 
            request.body["descricao"],
            request.body["data_hora"], 
            request.body["temporada"],
            request.body["numero"],
            RPG(id=request.body["rpg"]["id"]),
            (Usuario(id=jogador["id"]) for jogador in request.body["jogadores"]),
        )
        response = self.__use_case.cadastrar(form)

        return HttpResponse(
            status_code=200,
            body = response 
        )

    @classmethod
    def buscar_por_id(self, request: HttpRequest) -> HttpResponse: 
        response = self.__use_case.buscar_sessao_por_id(request.query_params["id"])
        return HttpResponse (
            status_code=200,
            body = response
        )
    
    @classmethod
    def atualizar(self, request: HttpRequest) -> HttpResponse: 
        form = Sessao()
        if("id" not in request.body):
            raise HttpError(HttpError.error_400("O campo 'id' é obrigatório."))
        form.set_id(request.body["id"])
        if "nome" in request.body:
            form.set_nome(request.body["nome"])
        if "descricao" in request.body:
            form.set_descricao(request.body["descricao"])
        if "data_hora" in request.body:
            form.set_data_hora(request.body["data_hora"])
        if "temporada" in request.body:
            form.set_temporada(request.body["temporada"])
        if "numero" in request.body:
            form.set_numero(request.body["numero"])
        if "jogadores" in request.body:
            form.set_jogadores(
                (Usuario(id=jogador["id"]) for jogador in request.body["jogadores"])
            )
        response = self.__use_case.atualizar(form)
        return HttpResponse (
            status_code=200,
            body = response
        )
    
    @classmethod
    def excluir(self, request: HttpRequest) -> HttpResponse: 
        response = self.__use_case.excluir(request.query_params["id"])
        return HttpResponse (
            status_code=200,
            body = response
        )