from src.data.interfaces import SessaoRepositoryInterface
from abc import ABC, abstractmethod
from typing import List, Dict

class ManterSessaoInterface(ABC):

    @abstractmethod
    def buscar_sessao_por_id(self, id: int) -> List[Dict]: pass

    @abstractmethod
    def buscar_sessoes(self) -> List[Dict]: pass

    @abstractmethod
    def cadastrar(self, sessao) -> Dict: pass

    @abstractmethod
    def atualizar(self, sessao) -> Dict: pass
    
    @abstractmethod
    def excluir(self, id: int) -> Dict: pass