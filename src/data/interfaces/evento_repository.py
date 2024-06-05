from abc import ABC, abstractmethod
from src.domain.models import Evento
from src.data.interfaces import BaseRepository

class EventoRepositoryInterface(BaseRepository[Evento]):
    pass
    
