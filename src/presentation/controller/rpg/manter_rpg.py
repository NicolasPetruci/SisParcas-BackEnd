from src.domain.use_cases.rpg import ManterRPGInterface
from src.domain.models import RPG, Genero, Mestre, Usuario
from src.presentation.http_types import HttpRequest, HttpResponse

class ManterRPGController():

    @classmethod
    def __init__(self, use_case: ManterRPGInterface):
        self.__use_case = use_case
    
    @classmethod
    def buscar(self, request: HttpRequest) -> HttpResponse: 
        response = self.__use_case.buscar_rpgs()
        return HttpResponse(
            status_code=200,
            body = response
        )

    @classmethod
    def cadastrar(self, request: HttpRequest) -> HttpResponse:

        form = RPG(
            0,
            request.body["nome"], 
            request.body["descricao"],
            mestre = Mestre(usuario=Usuario(id=request.payload.id)),
            generos = (Genero(id=genero["id"]) for genero in request.body["generos"])
        )
        response = self.__use_case.cadastrar(form)

        return HttpResponse(
            status_code=200,
            body = response 
        )

    @classmethod
    def buscar_por_id(self, request: HttpRequest) -> HttpResponse: 
        response = self.__use_case.buscar_rpg_por_id(request.query_params["id"])
        return HttpResponse (
            status_code=200,
            body = response
        )
    
    @classmethod
    def atualizar(self, request: HttpRequest) -> HttpResponse: 
        form = RPG()
        if("id" not in request.body):
            raise HttpError(HttpError.error_400("O campo 'id' é obrigatório."))
        form.set_id(request.body["id"])
        if "nome" in request.body:
            form.set_nome(request.body["nome"])
        if "descricao" in request.body:
            form.set_descricao(request.body["descricao"])
        if "generos" in request.body:
            form.set_generos(
                Genero(
                    request.body["generos"]["id"],
                    request.body["generos"]["descricao"],
                )
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