from abc import ABC, abstractmethod
from typing import List

class BuscarCargosUsuarioInterface(ABC):

    @abstractmethod
    def buscar_cargos_usuario(self, id: int) -> List: pass