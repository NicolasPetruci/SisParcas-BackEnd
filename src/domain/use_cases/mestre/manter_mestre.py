from src.data.interfaces import MestreRepositoryInterface
from abc import ABC, abstractmethod
from typing import List, Dict

class ManterMestreInterface(ABC):

    @abstractmethod
    def buscar_mestre_por_id(self, id: int) -> Dict: pass

    @abstractmethod
    def buscar_mestre_por_id_usuario(self, id: int) -> Dict: pass

    @abstractmethod
    def buscar_mestres(self) -> List[Dict]: pass

    @abstractmethod
    def cadastrar(self, mestre) -> Dict: pass

    @abstractmethod
    def atualizar(self, mestre) -> Dict: pass
    
    @abstractmethod
    def excluir(self, id: int) -> Dict: pass