from src.data.interfaces import MestreRepositoryInterface
from abc import ABC, abstractmethod
from typing import List, Dict

class InscricaoMestreInterface(ABC):

    @abstractmethod
    def deferir(self, id_usuario: int, id_rpg: int) -> Dict: pass

    @abstractmethod
    def indeferir(self, id_usuario: int, id_rpg: int) -> Dict: pass