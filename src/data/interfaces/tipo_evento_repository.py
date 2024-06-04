from abc import ABC, abstractmethod
from src.domain.models import TipoEvento
from src.data.interfaces import BaseRepository

class TipoEventoRepositoryInterface(BaseRepository[TipoEvento]):
    pass
    
