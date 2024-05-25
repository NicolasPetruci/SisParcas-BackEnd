from src.presentation import BaseController
from src.presentation.http_types import HttpRequest, HttpResponse
from src.domain.use_cases.cargo import CadastrarCargo as CadastrarCargoInterface
from src.domain.models.cargo import Cargo

class CadastrarCargoController(BaseController):

    @classmethod
    def __init__(self, use_case: CadastrarCargoInterface)->None:
        self.__use_case = use_case
    
    @classmethod
    def handle(self, http: HttpRequest) -> HttpResponse:
        form: Cargo = Cargo(0, http.body["descricao"])
        response = self.__use_case.cadastrar(form)

        return HttpResponse(
            status_code=200,
            body = { "data": response }
        )