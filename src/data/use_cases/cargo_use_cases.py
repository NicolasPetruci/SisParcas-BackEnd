from src.domain.models import Cargo
from src.domain.use_cases import CargoUseCasesInterface
from src.data.interfaces import CargoRepositoryInterface
from src.errors import HttpError
from typing import Dict, List

class CargoUseCases(CargoUseCasesInterface):

    @classmethod
    def __init__(self, repository: CargoRepositoryInterface):
        self.__repository = repository

    
    @classmethod
    def buscar_cargo_por_id(self, id: int) -> Dict:
        cargo = self.__repository.find_by_id(id)
        if cargo is None:
            raise HttpError(HttpError.error_404("Usuário não encontrado!"))
        return cargo.to_json()

    @classmethod
    def cadastrar(self, cargo: Cargo)->Dict:
        cargoInserir: Cargo = Cargo(None, cargo.descricao)
        return self.__repository.insert(cargoInserir).to_json()
    

    @classmethod
    def buscar_cargos(self) -> List[Dict]:
        cargos: List[Cargo] = self.__repository.find_all()
        return list(c.to_json() for c in cargos) 