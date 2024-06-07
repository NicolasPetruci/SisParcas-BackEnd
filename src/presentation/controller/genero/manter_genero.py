from src.domain.use_cases.genero import ManterGeneroInterface
from src.domain.models import Genero
from src.presentation.http_types import HttpRequest, HttpResponse

class ManterGeneroController():

    @classmethod
    def __init__(self, use_case: ManterGeneroInterface):
        self.__use_case = use_case
    
    @classmethod
    def buscar(self, request: HttpRequest) -> HttpResponse: 
        response = self.__use_case.buscar_generos()
        return HttpResponse(
            status_code=200,
            body = response
        )

    @classmethod
    def cadastrar(self, request: HttpRequest) -> HttpResponse:
        form = Genero(0, request.body["descricao"])
        response = self.__use_case.cadastrar(form)

        return HttpResponse(
            status_code=200,
            body = response 
        )

    @classmethod
    def buscar_por_id(self, request: HttpRequest) -> HttpResponse: 
        response = self.__use_case.buscar_genero_por_id(request.query_params["id"])
        return HttpResponse (
            status_code=200,
            body = response
        )
    
    @classmethod
    def atualizar(self, request: HttpRequest) -> HttpResponse: 
        form = Genero(request.body["id"], request.body["descricao"])
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