from src.domain.models import Usuario, Cargo
from src.domain.use_cases.usuario import BuscarCargosUsuarioInterface
from src.data.interfaces import UsuarioRepositoryInterface
from src.errors import HttpError
from src.main.adapters.auth import encrypt_password
from typing import Dict, List

class BuscarCargosUsuario(BuscarCargosUsuarioInterface):

    @classmethod
    def __init__(self, repository: UsuarioRepositoryInterface):
        self.__repository = repository

    
    @classmethod
    def buscar_cargos_usuario(self, id: int) -> Dict:
        usuario = self.__repository.find_by_id(id)
        if usuario is None:
            raise HttpError(HttpError.error_404("Usuario não encontrado."))
        return [cargo.to_json() for cargo in usuario.cargos]