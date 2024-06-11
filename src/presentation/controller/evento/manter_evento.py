from src.domain.use_cases.evento import ManterEventoInterface
from src.domain.models import Evento, TipoEvento
from src.presentation.http_types import HttpRequest, HttpResponse
from src.errors import HttpError

class ManterEventoController():

    @classmethod
    def __init__(self, use_case: ManterEventoInterface):
        self.__use_case = use_case
    
    @classmethod
    def buscar(self, request: HttpRequest) -> HttpResponse: 
        response = self.__use_case.buscar_eventos()
        return HttpResponse(
            status_code=200,
            body = response
        )

    @classmethod
    def cadastrar(self, request: HttpRequest) -> HttpResponse:

        form = Evento(
            0,
            request.body["nome"], 
            request.body["descricao"],
            request.body["local"],
            (request.body["online"].upper() == "SIM"),
            request.body["data_hora"], 
            TipoEvento(request.body["tipo_evento"]["id"], request.body["tipo_evento"]["descricao"])
        )
        response = self.__use_case.cadastrar(form)

        return HttpResponse(
            status_code=200,
            body = response 
        )

    @classmethod
    def buscar_por_id(self, request: HttpRequest) -> HttpResponse: 
        response = self.__use_case.buscar_evento_por_id(request.query_params["id"])
        return HttpResponse (
            status_code=200,
            body = response
        )
    
    @classmethod
    def atualizar(self, request: HttpRequest) -> HttpResponse: 
        form = Evento()
        if("id" not in request.body):
            raise HttpError(HttpError.error_400("O campo 'id' é obrigatório."))
        form.set_id(request.body["id"])
        if "nome" in request.body:
            form.set_nome(request.body["nome"])
        if "descricao" in request.body:
            form.set_descricao(request.body["descricao"])
        if "local" in request.body:
            form.set_local(request.body["local"])
        if "online" in request.body:
            form.set_online(request.body["online"].upper() == "SIM")
        if "data_hora" in request.body:
            form.set_data_hora(request.body["data_hora"])
        if "tipo_evento" in request.body:
            form.set_tipo_evento(
                TipoEvento(
                    request.body["tipo_evento"]["id"],
                    request.body["tipo_evento"]["descricao"],
                )
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