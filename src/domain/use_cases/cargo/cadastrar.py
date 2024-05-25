from abc import ABC, abstractmethod
from typing import Dict

class CadastrarCargo(ABC):

    @abstractmethod
    def cadastrar(self, cargo) -> Dict: pass