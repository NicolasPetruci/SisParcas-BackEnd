from src.data.interfaces import EventoRepositoryInterface
from abc import ABC, abstractmethod
from typing import List, Dict

class VisualizarEventosInterface(ABC):

    @abstractmethod
    def visualizar_eventos(self, data_inicial, data_final) -> List[Dict]: pass