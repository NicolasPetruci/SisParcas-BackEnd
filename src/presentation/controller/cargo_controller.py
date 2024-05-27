from src.domain.use_cases import CargoUseCasesInterface
from src.domain.models import Cargo
from src.presentation.http_types import HttpRequest, HttpResponse

class CargoController():
    @classmethod
    def __init__(self, use_case: CargoUseCasesInterface):
        self.__use_case = use_case
    
    @classmethod
    def buscar_cargos(self, request: HttpRequest) -> HttpResponse: 
        response = self.__use_case.buscar_cargos()
        return HttpResponse(
            status_code=200,
            body = {"data": response}
        )

    @classmethod
    def cadastrar_cargo(self, request: HttpRequest) -> HttpResponse:
        form = Cargo(0, request.body["descricao"])
        response = self.__use_case.cadastrar(form)

        return HttpResponse(
            status_code=200,
            body = { "data": response }
        )

    @classmethod
    def buscar_cargo_por_id(self, request: HttpRequest) -> HttpResponse: 
        response = self.__use_case.buscar_cargo_por_id(request.query_params["id"])
        return HttpResponse (
            status_code=200,
            body = {"data": response}
        )