from src.domain.use_cases.cargo import ManterCargoInterface
from src.domain.models import Cargo
from src.presentation.http_types import HttpRequest, HttpResponse

class ManterCargoController():

    @classmethod
    def __init__(self, use_case: ManterCargoInterface):
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
        form = Cargo(0, request.body["descricao"])
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
        form = Cargo(request.body["id"], request.body["descricao"])
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