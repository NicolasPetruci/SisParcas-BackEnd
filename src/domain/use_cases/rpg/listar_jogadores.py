from src.data.interfaces import RPGRepositoryInterface
from abc import ABC, abstractmethod
from typing import List, Dict

class ListarJogadoresInterface(ABC):

    @abstractmethod
    def buscar_jogadores_por_id_rpg(self, id: int) -> List[Dict]: pass