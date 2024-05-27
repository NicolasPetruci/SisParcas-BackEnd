from src.data.use_cases import CargoUseCases
from src.infra.db.repositories import CargoRepository
from src.presentation.controller import CargoController

def buscar_cargos_composer():
    repository = CargoRepository()
    use_case = CargoUseCases(repository)
    controller = CargoController(use_case)

    return controller.buscar_cargos