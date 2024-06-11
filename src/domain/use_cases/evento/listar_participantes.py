from src.data.interfaces import EventoRepositoryInterface
from abc import ABC, abstractmethod
from typing import List, Dict

class ListarParticipantesInterface(ABC):

    @abstractmethod
    def buscar_participantes_por_id_evento(self, id: int) -> List[Dict]: pass