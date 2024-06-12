from src.data.interfaces import SessaoRepositoryInterface
from abc import ABC, abstractmethod
from typing import List, Dict

class BuscarSessoesRPGInterface(ABC):

    @abstractmethod
    def buscar_sessoes_por_id_rpg(self, id_rpg) -> List[Dict]: pass
