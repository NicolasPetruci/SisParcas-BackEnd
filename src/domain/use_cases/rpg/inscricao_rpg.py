from src.data.interfaces import RPGRepositoryInterface
from abc import ABC, abstractmethod
from typing import List, Dict

class InscricaoRPGInterface(ABC):

    @abstractmethod
    def inscrever(self, id_usuario: int, id_rpg: int) -> Dict: pass

    @abstractmethod
    def desinscrever(self, id_usuario: int, id_rpg: int) -> Dict: pass