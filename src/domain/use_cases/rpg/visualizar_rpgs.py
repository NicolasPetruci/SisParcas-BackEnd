from src.data.interfaces import RPGRepositoryInterface
from abc import ABC, abstractmethod
from typing import List, Dict

class VisualizarRPGsInterface(ABC):

    @abstractmethod
    def visualizar_rpgs(self) -> List[Dict]: pass