from abc import ABC, abstractmethod
from src.domain.models import Sessao
from src.data.interfaces import BaseRepository

class SessaoRepositoryInterface(BaseRepository[Sessao]):
    pass
    
