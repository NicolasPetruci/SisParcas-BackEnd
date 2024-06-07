from src.domain.use_cases.usuario import LoginInterface
from src.domain.models import UsuarioLogin
from src.presentation.http_types import HttpRequest, HttpResponse

class LoginController():

    @classmethod
    def __init__(self, use_case: LoginInterface):
        self.__use_case = use_case

    @classmethod
    def login(self, request: HttpRequest):
        form = UsuarioLogin(request.body["email"], request.body["senha"])
        response_body = self.__use_case.login(form)

        return HttpResponse (
            status_code=200,
            body = response_body
        )