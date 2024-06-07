from src.domain.use_cases.mestre import InscricaoMestreInterface
from src.domain.models import Mestre, Usuario
from src.presentation.http_types import HttpRequest, HttpResponse

class InscricaoMestreController():

    @classmethod
    def __init__(self, use_case: InscricaoMestreInterface):
        self.__use_case = use_case
    
    @classmethod
    def deferir(self, request: HttpRequest) -> HttpResponse: 
        response = self.__use_case.deferir(request.query_params["id_usuario"], request.query_params["id_mestre"])
        return HttpResponse(
            status_code=200,
            body = response
        )

    @classmethod
    def indeferir(self, request: HttpRequest) -> HttpResponse: 
        response = self.__use_case.indeferir(request.query_params["id_usuario"], request.query_params["id_mestre"])
        return HttpResponse(
            status_code=200,
            body = response
        )