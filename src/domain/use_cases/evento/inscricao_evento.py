from src.data.interfaces import EventoRepositoryInterface
from abc import ABC, abstractmethod
from typing import List, Dict

class InscricaoEventoInterface(ABC):

    @abstractmethod
    def inscrever(self, id_usuario: int, id_evento: int) -> Dict: pass

    @abstractmethod
    def desinscrever(self, id_usuario: int, id_evento: int) -> Dict: pass