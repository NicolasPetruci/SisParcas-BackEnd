from src.domain.use_cases.cargo import BuscarCargos as BuscarCargosInterface
from src.data.interfaces import CargoRepositoryInterface 
from src.domain.models import Cargo
from typing import Dict, List


class BuscarCargos(BuscarCargosInterface):

    @classmethod
    def __init__(self, repository: CargoRepositoryInterface) -> None:
        self.__repository = repository

    @classmethod
    def buscar_cargos(self) -> List[Dict]:
        cargos: List[Cargo] = self.__repository.find_all()
        return list(c.to_json() for c in cargos) 
        

