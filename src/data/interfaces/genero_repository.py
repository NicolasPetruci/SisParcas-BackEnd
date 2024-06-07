from abc import ABC, abstractmethod
from src.domain.models import Genero
from src.data.interfaces import BaseRepository

class GeneroRepositoryInterface(BaseRepository[Genero]):
    pass
    
