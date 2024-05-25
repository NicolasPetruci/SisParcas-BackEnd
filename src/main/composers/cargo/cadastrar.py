from src.infra.db.repositories import CargoRepository
from src.data.use_cases.cargo import CadastrarCargo
from src.presentation.controller.cargo import CadastrarCargoController
from src.presentation.http_types import HttpRequest

def cadastrar_cargo_composer():
    repository = CargoRepository()
    use_case = CadastrarCargo(repository)
    controller = CadastrarCargoController(use_case)

    return controller.handle
