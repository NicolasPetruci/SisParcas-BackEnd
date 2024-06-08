from src.domain.use_cases.rpg import InscricaoRPGInterface
from src.domain.models import RPG
from src.presentation.http_types import HttpRequest, HttpResponse

class InscricaoRPGController():

    @classmethod
    def __init__(self, use_case: InscricaoRPGInterface):
        self.__use_case = use_case
    
    @classmethod
    def inscrever(self, request: HttpRequest) -> HttpResponse: 
        response = self.__use_case.inscrever(
            request.query_params["id_usuario"],
            request.query_params["id_rpg"]
            )
        return HttpResponse (
            status_code=200,
            body = response
        )

    @classmethod
    def desinscrever(self, request: HttpRequest) -> HttpResponse: 
        response = self.__use_case.desinscrever(
            request.query_params["id_usuario"],
            request.query_params["id_rpg"]
            )
        return HttpResponse (
            status_code=200,
            body = response
        )