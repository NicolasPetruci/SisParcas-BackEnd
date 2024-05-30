from .base_repository import BaseRepository
from src.domain.models import Usuario
from abc import abstractmethod

class UsuarioRepositoryInterface(BaseRepository[Usuario]):

    @abstractmethod
    def find_user_by_email(self, email: str): pass

