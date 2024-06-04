from src.domain.models import Usuario, UsuarioLogin
from src.domain.use_cases.usuario import LoginInterface
from src.data.interfaces import UsuarioRepositoryInterface
from src.main.adapters.auth import check_encrypted_password, encode_token, Payload
from src.errors.http_error import HttpError

class Login(LoginInterface):

    @classmethod
    def __init__(self, repository: UsuarioRepositoryInterface):
        self.__repository = repository
    
    @classmethod
    def __buscar_usuario_por_email(self, email: str) -> Usuario:
        return usuario

    @classmethod
    def login(self, loginInfo: UsuarioLogin) -> Payload:
        usuario = self.__repository.find_user_by_email(loginInfo.email)
        if(usuario is None):
            raise HttpError(HttpError.error_401("Email ou senha incorretos."))
        if(
            usuario.email == loginInfo.email and
            check_encrypted_password(loginInfo.senha, usuario.senha)
        ):
            payload = Payload(usuario.email, usuario.cargo.descricao, usuario.id)
            token = encode_token(payload)
            return { "token": token }
        else:
            raise HttpError(HttpError.error_401("Email ou senha incorretos."))
            
            
