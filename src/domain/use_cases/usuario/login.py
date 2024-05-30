from abc import ABC, abstractmethod
from src.domain.models import UsuarioLogin
from src.main.adapters.auth import Payload

class LoginInterface(ABC):

    @abstractmethod
    def login(self, loginInfo: UsuarioLogin) -> Payload: pass