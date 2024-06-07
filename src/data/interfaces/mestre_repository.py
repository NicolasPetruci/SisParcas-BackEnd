from abc import ABC, abstractmethod
from src.domain.models import Mestre
from src.data.interfaces import BaseRepository

class MestreRepositoryInterface(BaseRepository[Mestre]):
    pass
    
