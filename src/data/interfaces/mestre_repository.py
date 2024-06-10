from abc import ABC, abstractmethod
from src.domain.models import Mestre
from src.data.interfaces import BaseRepository

class MestreRepositoryInterface(BaseRepository[Mestre]):
    
    @abstractmethod
    def find_by_id_usuario(self, id_usuario: int) -> Mestre: pass
    
