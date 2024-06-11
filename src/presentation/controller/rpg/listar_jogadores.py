from src.domain.use_cases.rpg import ListarJogadoresInterface
from src.presentation.http_types import HttpRequest, HttpResponse

class ListarJogadoresController():

    @classmethod
    def __init__(self, use_case: ListarJogadoresInterface):
        self.__use_case = use_case
    
    @classmethod
    def listar_jogadores(self, request: HttpRequest) -> HttpResponse: 
        response = self.__use_case.buscar_jogadores_por_id_rpg(request.query_params["id_rpg"])
        return HttpResponse(
            status_code=200,
            body = response
        )