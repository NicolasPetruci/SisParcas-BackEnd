from abc import ABC, abstractmethod
from src.domain.models import Cargo
from src.data.interfaces import BaseRepository

class CargoRepositoryInterface(BaseRepository[Cargo]):
    pass
    
