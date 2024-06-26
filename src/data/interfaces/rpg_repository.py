from abc import ABC, abstractmethod
from src.domain.models import RPG
from src.data.interfaces import BaseRepository

class RPGRepositoryInterface(BaseRepository[RPG]):
    pass
    
