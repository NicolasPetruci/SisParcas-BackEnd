from src.domain.models import RPG, Usuario
from src.domain.use_cases.rpg import InscricaoRPGInterface
from src.data.interfaces import RPGRepositoryInterface, UsuarioRepositoryInterface
from src.errors import HttpError
from typing import Dict, List

class InscricaoRPG(InscricaoRPGInterface):

    @classmethod
    def __init__(
            self,
            repository: RPGRepositoryInterface,
            usuario_repository: UsuarioRepositoryInterface 
            ):
        self.__repository = repository
        self.__usuario_repository = usuario_repository
    
    @classmethod
    def inscrever(self, id_usuario: int, id_rpg: int) -> Dict:
        rpg: RPG = self.__repository.find_by_id(id_rpg)
        if rpg is None:
            raise HttpError(HttpError.error_404("RPG não encontrado."))
        usuario: Usuario = self.__usuario_repository.find_by_id(id_usuario)
        if usuario is None:
            raise HttpError(HttpError.error_404("Usuario não encontrado."))
        if usuario in rpg.jogadores:
            raise HttpError(HttpError.error_400("Jogador já inscrito."))
        rpg.adicionar_jogador(usuario)
        rpg_atualizado = self.__repository.update(rpg)
        return {
            "rpg": rpg_atualizado.to_json(),
            "message": "Inscrição realizada com sucesso.",
        }

    @classmethod
    def desinscrever(self, id_usuario: int, id_rpg: int) -> Dict:
        rpg: RPG = self.__repository.find_by_id(id_rpg)
        if rpg is None:
            raise HttpError(HttpError.error_404("RPG não encontrado."))
        usuario: Usuario = self.__usuario_repository.find_by_id(id_usuario)
        if usuario is None:
            raise HttpError(HttpError.error_404("Usuario não encontrado."))
        if usuario not in rpg.jogadores:
            raise HttpError(HttpError.error_400("Jogador não está inscrito."))
        rpg.remover_jogador(usuario)
        rpg_atualizado = self.__repository.update(rpg)
        return {
            "rpg": rpg_atualizado.to_json(),
            "message": "Inscrição cancelada com sucesso.",
        }