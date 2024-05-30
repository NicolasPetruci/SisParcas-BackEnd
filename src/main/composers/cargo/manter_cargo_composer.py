from src.data.use_cases.cargo import ManterCargo
from src.infra.db.repositories import CargoRepository
from src.presentation.controller.cargo import ManterCargoController

def compose_methods():
    repository = CargoRepository()
    use_case = ManterCargo(repository)
    controller = ManterCargoController(use_case)

    return controller


def atualizar_cargo_composer():
    controller = compose_methods()
    return controller.atualizar

def buscar_cargos_composer():
    controller = compose_methods()
    return controller.buscar

def buscar_cargo_por_id_composer():
    controller = compose_methods()
    return controller.buscar_por_id

def excluir_cargo_composer():
    controller = compose_methods()
    return controller.excluir

def cadastrar_cargo_composer():
    controller = compose_methods()
    return controller.cadastrar

def atualizar_cargo_composer():
    controller = compose_methods()
    return controller.atualizar