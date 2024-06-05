from src.domain.use_cases.evento import InscricaoEventoInterface
from src.domain.models import Evento
from src.presentation.http_types import HttpRequest, HttpResponse

class InscricaoEventoController():

    @classmethod
    def __init__(self, use_case: InscricaoEventoInterface):
        self.__use_case = use_case
    
    @classmethod
    def inscrever(self, request: HttpRequest) -> HttpResponse: 
        response = self.__use_case.inscrever(
            request.query_params["idUsuario"],
            request.query_params["idEvento"]
            )
        return HttpResponse (
            status_code=200,
            body = {"data": response}
        )

    @classmethod
    def desinscrever(self, request: HttpRequest) -> HttpResponse: 
        response = self.__use_case.desinscrever(
            request.query_params["idUsuario"],
            request.query_params["idEvento"]
            )
        return HttpResponse (
            status_code=200,
            body = {"data": response}
        )