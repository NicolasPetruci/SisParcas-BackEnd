from src.domain.models import Cargo
from src.domain.use_cases import ManterCargoInterface
from src.data.interfaces import CargoRepositoryInterface
from src.errors import HttpError
from typing import Dict, List

class ManterCargo(ManterCargoInterface):

    @classmethod
    def __init__(self, repository: CargoRepositoryInterface):
        self.__repository = repository

    
    @classmethod
    def buscar_cargo_por_id(self, id: int) -> Dict:
        cargo = self.__repository.find_by_id(id)
        if cargo is None:
            raise HttpError(HttpError.error_404("Cargo não encontrado."))
        return cargo.to_json()

    @classmethod
    def cadastrar(self, cargo: Cargo)->Dict:
        novo_cargo: Cargo = Cargo(None, cargo.descricao)
        return {
            "cargo": self.__repository.insert(novo_cargo).to_json(),
            "message": "Usuario cadastrado com sucesso.",
        }
    

    @classmethod
    def buscar_cargos(self) -> List[Dict]:
        cargos: List[Cargo] = self.__repository.find_all()
        return list(c.to_json() for c in cargos) 
    
    @classmethod
    def atualizar(self, cargo: Cargo) -> Dict:
        cargo_atualizado = self.__repository.update(cargo)
        if cargo_atualizado is None:
            raise HttpError(HttpError.error_404("Cargo não encontrado."))
        return {
            "cargo": cargo_atualizado.to_json(),
            "message": "Usuario cadastrado com sucesso.",
        }
    
    @classmethod
    def excluir(self, id: int) -> Dict: 
        cargo_excluido = self.__repository.delete_by_id(id)
        if cargo_excluido is None:
            raise HttpError(HttpError.error_404("Cargo não encontrado."))
        return {
            "cargo": cargo_excluido.to_json(),
            "message": "Usuario cadastrado com sucesso.",
        }