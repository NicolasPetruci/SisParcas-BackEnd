from abc import ABC, abstractmethod
from src.domain.models import Evento
from src.data.interfaces import BaseRepository
from typing import List
from datetime import datetime

class EventoRepositoryInterface(BaseRepository[Evento]):
    
    @abstractmethod
    def find_all_between_dates(data_inicial: datetime, data_final: datetime) -> List[Evento]: pass
    
