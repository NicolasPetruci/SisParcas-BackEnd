from abc import ABC, abstractmethod
from typing import List, Dict
from src.domain.models import Cargo

class CargoUseCasesInterface(ABC):

    @abstractmethod
    def buscar_cargo_por_id(self, id: int) -> List[Dict]: pass

    @abstractmethod
    def buscar_cargos(self) -> List[Dict]: pass

    @abstractmethod
    def cadastrar(self, cargo) -> Dict: pass

    @abstractmethod
    def atualizar(self, cargo) -> Dict: pass
    
    @abstractmethod
    def excluir(self, id: int) -> Dict: pass