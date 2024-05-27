from abc import ABC, abstractmethod
from typing import List, Dict

class CargoUseCasesInterface(ABC):

    @abstractmethod
    def buscar_cargo_por_id(self, id: int) -> List[Dict]: pass

    @abstractmethod
    def buscar_cargos(self) -> List[Dict]: pass

    @abstractmethod
    def cadastrar(self, cargo) -> Dict: pass