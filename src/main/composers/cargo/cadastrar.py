from src.infra.db.repositories import CargoRepository
from src.data.use_cases import CargoUseCases
from src.presentation.controller import CargoController

def cadastrar_cargo_composer():
    repository = CargoRepository()
    use_case = CargoUseCases(repository)
    controller = CargoController(use_case)

    return controller.cadastrar_cargo
