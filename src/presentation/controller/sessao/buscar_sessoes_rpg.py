from src.domain.use_cases.sessao import BuscarSessoesRPGInterface
from src.domain.models import Sessao, RPG, Usuario
from src.presentation.http_types import HttpRequest, HttpResponse

class BuscarSessoesRPGController():

    @classmethod
    def __init__(self, use_case: BuscarSessoesRPGInterface):
        self.__use_case = use_case
    
    @classmethod
    def buscar_por_id_rpg(self, request: HttpRequest) -> HttpResponse: 
        response = self.__use_case.buscar_sessoes_por_id_rpg(request.query_params["id_rpg"])
        return HttpResponse(
            status_code=200,
            body = response
        )