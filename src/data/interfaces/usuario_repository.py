from .base_repository import BaseRepository
from src.domain.models import Usuario

class UsuarioRepositoryInterface(BaseRepository[Usuario]):
    pass