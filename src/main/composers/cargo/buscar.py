from src.data.use_cases.cargo import BuscarCargos
from src.presentation.controller.cargo import BuscarCargosController
from src.infra.db.repositories import CargoRepository

def buscar_cargos_composer():
    repository = CargoRepository()
    use_case = BuscarCargos(repository)
    controller = BuscarCargosController(use_case)

    return controller.handle