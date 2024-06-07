from src.domain.use_cases.cargo import ManterMestreInterface
from src.domain.models import Mestre
from src.presentation.http_types import HttpRequest, HttpResponse

class ManterMestreController():

    @classmethod
    def __init__(self, use_case: ManterMestreInterface):
        self.__use_case = use_case
    
    @classmethod
    def buscar(self, request: HttpRequest) -> HttpResponse: 
        response = self.__use_case.buscar_cargos()
        return HttpResponse(
            status_code=200,
            body = {"data": response}
        )

    @classmethod
    def cadastrar(self, request: HttpRequest) -> HttpResponse:
        form = Mestre()
        form.set_usuario(request.body["usuario"]["id"])
        response = self.__use_case.cadastrar(form)

        return HttpResponse(
            status_code=200,
            body = { "data": response }
        )

    @classmethod
    def buscar_por_id(self, request: HttpRequest) -> HttpResponse: 
        response = self.__use_case.buscar_cargo_por_id(request.query_params["id"])
        return HttpResponse (
            status_code=200,
            body = {"data": response}
        )
    
    @classmethod
    def atualizar(self, request: HttpRequest) -> HttpResponse: 
        form = Mestre(request.body["id"], request.body["descricao"])
        response = self.__use_case.atualizar(form)
        return HttpResponse (
            status_code=200,
            body = {"data": response}
        )
    
    @classmethod
    def excluir(self, request: HttpRequest) -> HttpResponse: 
        response = self.__use_case.excluir(request.query_params["id"])
        return HttpResponse (
            status_code=200,
            body = {"data": response}
        )