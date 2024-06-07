from abc import ABC, abstractmethod
from typing import List, Dict
from src.domain.models import Genero

class ManterGeneroInterface(ABC):

    @abstractmethod
    def buscar_generos(self) -> List[Dict]: pass

    @abstractmethod
    def cadastrar(self, genero) -> Dict: pass

    @abstractmethod
    def atualizar(self, genero) -> Dict: pass
    
    @abstractmethod
    def excluir(self, id: int) -> Dict: pass