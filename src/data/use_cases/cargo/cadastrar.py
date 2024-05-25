from src.domain.use_cases.cargo import CadastrarCargo as CadastrarCargoInterface
from src.data.interfaces import CargoRepositoryInterface 
from src.domain.models import Cargo
from typing import Dict

class CadastrarCargo(CadastrarCargoInterface):
    
    def __init__(self, repository: CargoRepositoryInterface):
        self.__repository = repository

    def cadastrar(self, cargo: Cargo)->Dict:
        cargoInserir: Cargo = Cargo(None, cargo.descricao)
        self.__repository.insert(cargoInserir)