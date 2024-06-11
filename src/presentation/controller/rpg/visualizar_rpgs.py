from src.domain.use_cases.rpg import VisualizarRPGsInterface
from src.presentation.http_types import HttpRequest, HttpResponse

class VisualizarRPGsController():

    @classmethod
    def __init__(self, use_case: VisualizarRPGsInterface):
        self.__use_case = use_case
    
    @classmethod
    def visualizar_rpgs(self, request: HttpRequest) -> HttpResponse: 
        response = self.__use_case.visualizar_rpgs()
        return HttpResponse(
            status_code=200,
            body = response
        )