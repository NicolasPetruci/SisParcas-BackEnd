from src.data.interfaces import EventoRepositoryInterface
from abc import ABC, abstractmethod
from typing import List, Dict

class ManterEventoInterface(ABC):

    @abstractmethod
    def buscar_evento_por_id(self, id: int) -> List[Dict]: pass

    @abstractmethod
    def buscar_eventos(self) -> List[Dict]: pass

    @abstractmethod
    def cadastrar(self, evento) -> Dict: pass

    @abstractmethod
    def atualizar(self, evento) -> Dict: pass
    
    @abstractmethod
    def excluir(self, id: int) -> Dict: pass