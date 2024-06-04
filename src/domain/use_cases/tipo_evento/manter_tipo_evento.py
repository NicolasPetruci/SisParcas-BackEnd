from abc import ABC, abstractmethod
from typing import List, Dict
from src.domain.models import TipoEvento

class ManterTipoEventoInterface(ABC):

    @abstractmethod
    def buscar_tipo_evento_por_id(self, id: int) -> List[Dict]: pass

    @abstractmethod
    def buscar_tipo_eventos(self) -> List[Dict]: pass

    @abstractmethod
    def cadastrar(self, tipo_evento) -> Dict: pass

    @abstractmethod
    def atualizar(self, tipo_evento) -> Dict: pass
    
    @abstractmethod
    def excluir(self, id: int) -> Dict: pass