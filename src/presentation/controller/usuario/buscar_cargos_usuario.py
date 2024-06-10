from src.domain.use_cases.usuario import BuscarCargosUsuarioInterface
from src.domain.models import Usuario, Cargo
from src.presentation.http_types import HttpRequest, HttpResponse

class BuscarCargosUsuarioController():

    @classmethod
    def __init__(self, use_case: BuscarCargosUsuarioInterface):
        self.__use_case = use_case

    @classmethod
    def buscar_cargos_usuario(self, request: HttpRequest) -> HttpResponse: 
        response = self.__use_case.buscar_cargos_usuario(request.payload.id)
        return HttpResponse (
            status_code=200,
            body = response
        )