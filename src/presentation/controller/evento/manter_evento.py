from src.domain.use_cases.evento import ManterEventoInterface
from src.domain.models import Evento
from src.presentation.http_types import HttpRequest, HttpResponse

class ManterEventoController():

    @classmethod
    def __init__(self, use_case: ManterEventoInterface):
        self.__use_case = use_case
    
    @classmethod
    def buscar(self, request: HttpRequest) -> HttpResponse: 
        response = self.__use_case.buscar_eventos()
        return HttpResponse(
            status_code=200,
            body = {"data": response}
        )

    @classmethod
    def cadastrar(self, request: HttpRequest) -> HttpResponse:

        form = Evento(
        0,
        request.body["nome"], 
        request.body["descricao"],
        request.body["local"],
        request.body["data_hora"], 
        request.body["tipo_evento"], 
        request.body["participantes"]
        )
        response = self.__use_case.cadastrar(form)

        return HttpResponse(
            status_code=200,
            body = { "data": response }
        )

    @classmethod
    def buscar_por_id(self, request: HttpRequest) -> HttpResponse: 
        response = self.__use_case.buscar_evento_por_id(request.query_params["id"])
        return HttpResponse (
            status_code=200,
            body = {"data": response}
        )
    
    @classmethod
    def atualizar(self, request: HttpRequest) -> HttpResponse: 
        form = Evento(
                    request.body["id"],
                    request.body["nome"], 
                    request.body["descricao"],
                    request.body["local"],
                    request.body["data_hora"], 
                    request.body["tipo_evento"], 
                    request.body["participantes"]
                )
        response = self.__use_case.atualizar(form)
        return HttpResponse (
            status_code=200,
            body = {"data": response}
        )
    
    @classmethod
    def excluir(self, request: HttpRequest) -> HttpResponse: 
        response = self.__use_case.excluir(request.query_params["id"])
        return HttpResponse (
            status_code=200,
            body = {"data": response}
        )