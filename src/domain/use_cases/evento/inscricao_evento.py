from src.data.interfaces import EventoRepositoryInterface
from abc import ABC, abstractmethod
from typing import List, Dict

class InscreverEventoInterface(ABC):

    @abstractmethod
    def inscrever(self, id: int) -> Dict: pass

    @abstractmethod
    def desinscrever(self, id: int) -> Dict: pass