from src.domain.use_cases.evento import ListarParticipantesInterface
from src.presentation.http_types import HttpRequest, HttpResponse

class ListarParticipantesController():

    @classmethod
    def __init__(self, use_case: ListarParticipantesInterface):
        self.__use_case = use_case
    
    @classmethod
    def listar_participantes(self, request: HttpRequest) -> HttpResponse: 
        response = self.__use_case.buscar_participantes_por_id_evento(request.query_params["id_evento"])
        return HttpResponse(
            status_code=200,
            body = response
        )