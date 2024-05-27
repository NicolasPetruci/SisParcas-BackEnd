from abc import ABC, abstractmethod
from typing import List, Dict

class BuscarCargos(ABC):

    @abstractmethod
    def buscar_cargos() -> List[Dict]: pass

