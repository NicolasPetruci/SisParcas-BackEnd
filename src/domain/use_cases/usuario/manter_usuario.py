from src.data.interfaces import UsuarioRepositoryInterface
from abc import ABC, abstractmethod

class ManterUsuarioInterface(ABC):

    @abstractmethod
    def buscar_usuario_por_id(self, id: int) -> List[Dict]: pass

    @abstractmethod
    def buscar_usuarios(self) -> List[Dict]: pass

    @abstractmethod
    def cadastrar(self, usuario) -> Dict: pass

    @abstractmethod
    def atualizar(self, usuario) -> Dict: pass
    
    @abstractmethod
    def excluir(self, id: int) -> Dict: pass