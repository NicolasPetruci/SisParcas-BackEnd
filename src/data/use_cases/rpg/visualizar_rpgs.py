from src.domain.use_cases.rpg import VisualizarRPGsInterface
from src.domain.models import RPG, Usuario
from src.data.interfaces import RPGRepositoryInterface
from src.errors import HttpError
from typing import List, Dict
from datetime import datetime

class VisualizarRPGs(VisualizarRPGsInterface):

    @classmethod
    def __init__(self, repository: RPGRepositoryInterface):
        self.__repository = repository

    @classmethod
    def visualizar_rpgs(self) -> List[Dict]: 
        rpgs: List[RPG] = self.__repository.find_all()
        if rpgs is None:
            raise HttpError(HttpError.error_404("RPG não encontrado."))
        return [
                self.rpg_relatorio_to_json(index, rpg) 
                for index, rpg in enumerate(rpgs, start=1)
               ]

    @classmethod
    def rpg_relatorio_to_json(self, index: int, rpg: RPG):
        return {
            "numero": index,
            "nome": rpg.nome,
            "mestre": rpg.mestre.usuario.nome,
            "generos": ''.join([genero.descricao for genero in rpg.generos]),
            "numero_jogadores": len(rpg.jogadores) 
        }