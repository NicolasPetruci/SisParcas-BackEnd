from src.domain.use_cases.rpg import ListarJogadoresInterface
from src.domain.models import RPG, Usuario
from src.data.interfaces import RPGRepositoryInterface
from src.errors import HttpError
from typing import List, Dict

class ListarJogadores(ListarJogadoresInterface):

    @classmethod
    def __init__(self, repository: RPGRepositoryInterface):
        self.__repository = repository

    @classmethod
    def buscar_jogadores_por_id_rpg(self, id: int) -> List[Dict]: 
        rpg: RPG = self.__repository.find_by_id(id)
        if rpg is None:
            raise HttpError(HttpError.error_404("RPG não encontrado."))
        if not rpg.jogadores:
            raise HttpError(HttpError.error_400("RPG não possui jogadores."))
        return [
                self.jogador_relatorio_to_json(index, jogador) 
                for index, jogador in enumerate(rpg.jogadores, start=1)
               ]

    @classmethod
    def jogador_relatorio_to_json(self, index: int, jogador: Usuario):
        return {
            "numero": index,
            "nome": jogador.nome,
            "telefone": jogador.telefone,
        }