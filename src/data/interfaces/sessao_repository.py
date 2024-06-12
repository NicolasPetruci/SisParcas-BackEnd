from abc import ABC, abstractmethod
from src.domain.models import Sessao
from src.data.interfaces import BaseRepository

class SessaoRepositoryInterface(BaseRepository[Sessao]):
    
    @abstractmethod
    def find_all_by_id_rpg(self, id_rpg: int): pass
    
