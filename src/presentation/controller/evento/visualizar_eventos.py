from src.domain.use_cases.evento import VisualizarEventosInterface
from src.presentation.http_types import HttpRequest, HttpResponse

class VisualizarEventosController():

    @classmethod
    def __init__(self, use_case: VisualizarEventosInterface):
        self.__use_case = use_case
    
    @classmethod
    def visualizar_eventos(self, request: HttpRequest) -> HttpResponse: 
        response = self.__use_case.visualizar_eventos(
                request.query_params["data_inicial"],
                request.query_params["data_final"]
            )
        return HttpResponse(
            status_code=200,
            body = response
        )