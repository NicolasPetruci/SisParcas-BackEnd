from src.domain.use_cases.mestre import ManterMestreInterface
from src.domain.models import Mestre
from src.presentation.http_types import HttpRequest, HttpResponse

class BuscarMestreLogadoController():

    @classmethod
    def __init__(self, use_case: ManterMestreInterface):
        self.__use_case = use_case

    @classmethod
    def buscar_mestre_logado(self, request: HttpRequest) -> HttpResponse: 
        response = self.__use_case.buscar_mestre_por_id_usuario(request.payload.id, request.payload.cargos)
        return HttpResponse (
            status_code=200,
            body = response
        )