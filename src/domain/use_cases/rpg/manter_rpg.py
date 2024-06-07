from src.data.interfaces import RPGRepositoryInterface
from abc import ABC, abstractmethod
from typing import List, Dict

class ManterRPGInterface(ABC):

    @abstractmethod
    def buscar_rpg_por_id(self, id: int) -> List[Dict]: pass

    @abstractmethod
    def buscar_rpgs(self) -> List[Dict]: pass

    @abstractmethod
    def cadastrar(self, rpg) -> Dict: pass

    @abstractmethod
    def atualizar(self, rpg) -> Dict: pass
    
    @abstractmethod
    def excluir(self, id: int) -> Dict: pass