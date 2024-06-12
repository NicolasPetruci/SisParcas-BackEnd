from src.domain.models import Sessao
from src.domain.use_cases.sessao import BuscarSessoesRPGInterface
from src.data.interfaces import SessaoRepositoryInterface
from src.errors import HttpError
from typing import Dict, List

class BuscarSessoesRPG(BuscarSessoesRPGInterface):

    @classmethod
    def __init__(self, repository: SessaoRepositoryInterface):
        self.__repository = repository

    @classmethod
    def buscar_sessoes_por_id_rpg(self, id_rpg: int) -> List[Dict]:
        sessoes: List[Sessao] = self.__repository.find_all_by_id_rpg(id_rpg)
        return list(c.to_json() for c in sessoes) 