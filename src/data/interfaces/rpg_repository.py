from abc import ABC, abstractmethod
from src.domain.models import Rpg
from src.data.interfaces import BaseRepository

class RpgRepositoryInterface(BaseRepository[Rpg]):
    pass
    
