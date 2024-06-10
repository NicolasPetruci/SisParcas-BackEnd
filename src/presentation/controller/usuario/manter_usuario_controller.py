from src.domain.use_cases.usuario import ManterUsuarioInterface
from src.domain.models import Usuario, Cargo
from src.presentation.http_types import HttpRequest, HttpResponse

class ManterUsuarioController():

    @classmethod
    def __init__(self, use_case: ManterUsuarioInterface):
        self.__use_case = use_case
    
    @classmethod
    def buscar(self, request: HttpRequest) -> HttpResponse: 
        response = self.__use_case.buscar_usuarios()
        return HttpResponse(
            status_code=200,
            body = response
        )

    @classmethod
    def cadastrar(self, request: HttpRequest) -> HttpResponse:
        form = Usuario(
            None, 
            request.body["nome"],
            request.body["email"],
            request.body["telefone"],
            request.body["senha"],
            request.body["aniversario"],
            [Cargo(id = cargo["id"]) for cargo in request.body["cargos"]]
            )
        response = self.__use_case.cadastrar(form)

        return HttpResponse(
            status_code=200,
            body = response
        )

    @classmethod
    def buscar_por_id(self, request: HttpRequest) -> HttpResponse: 
        response = self.__use_case.buscar_usuario_por_id(request.query_params["id"])
        return HttpResponse (
            status_code=200,
            body = response
        )
    
    @classmethod
    def atualizar(self, request: HttpRequest) -> HttpResponse: 
        form = Usuario(
            request.body["id"],
            request.body["nome"],
            request.body["email"],
            request.body["telefone"],
            None,
            request.body["aniversario"],
            [Cargo(id = cargo["id"]) for cargo in request.body["cargos"]]
        )
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