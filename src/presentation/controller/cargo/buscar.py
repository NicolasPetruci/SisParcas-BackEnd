from src.presentation import BaseController
from src.presentation.http_types import HttpRequest, HttpResponse
from src.domain.use_cases.cargo import BuscarCargos as BuscarCargosInterface
from src.domain.models import Cargo
from typing import Dict

class BuscarCargosController(BaseController):

    @classmethod
    def __init__(self, use_case: BuscarCargosInterface):
        self.__use_case = use_case
    
    @classmethod
    def handle(self, request: HttpRequest) -> Dict: 
        response = self.__use_case.buscar_cargos()
        return HttpResponse(
            status_code=200,
            body = {"data": response}
        )
