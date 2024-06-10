from src.domain.use_cases.mestre import ManterMestreInterface
from src.domain.models import Mestre, Usuario
from src.presentation.http_types import HttpRequest, HttpResponse

class ManterMestreController():

    @classmethod
    def __init__(self, use_case: ManterMestreInterface):
        self.__use_case = use_case
    
    @classmethod
    def buscar(self, request: HttpRequest) -> HttpResponse: 
        response = self.__use_case.buscar_mestres()
        return HttpResponse(
            status_code=200,
            body = response
        )

    @classmethod
    def cadastrar(self, request: HttpRequest) -> HttpResponse:
        form = Mestre().set_ativo(request.body["ativo"]).set_usuario(Usuario(id=request.payload.id))
        response = self.__use_case.cadastrar(form)

        return HttpResponse(
            status_code=200,
            body = response
        )

    @classmethod
    def buscar_por_id(self, request: HttpRequest) -> HttpResponse: 
        response = self.__use_case.buscar_mestre_por_id(request.query_params["id"])
        return HttpResponse (
            status_code=200,
            body = response
        )
    
    @classmethod
    def atualizar(self, request: HttpRequest) -> HttpResponse: 
        form = Mestre(request.body["id"], request.body["ativo"], Usuario(id=request.body["usuario"]["id"]))
        response = self.__use_case.atualizar(form)
        return HttpResponse (
            status_code=200,
            body = response
        )
    
    @classmethod
    def excluir(self, request: HttpRequest) -> HttpResponse: 
        response = self.__use_case.excluir(request.query_params["id"])
        return HttpResponse (
            status_code=200,
            body = response
        )