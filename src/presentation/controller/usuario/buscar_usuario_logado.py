from src.domain.use_cases.usuario import ManterUsuarioInterface
from src.domain.models import Usuario, Cargo
from src.presentation.http_types import HttpRequest, HttpResponse

class BuscarUsuarioLogadoController():

    @classmethod
    def __init__(self, use_case: ManterUsuarioInterface):
        self.__use_case = use_case

    @classmethod
    def buscar_usuario_logado(self, request: HttpRequest) -> HttpResponse: 
        response = self.__use_case.buscar_usuario_por_id(request.payload.id)
        return HttpResponse (
            status_code=200,
            body = response
        )