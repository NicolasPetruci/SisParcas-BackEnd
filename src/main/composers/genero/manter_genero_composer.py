from src.data.use_cases.genero import ManterGenero
from src.infra.db.repositories import GeneroRepository
from src.presentation.controller.genero import ManterGeneroController

def compose_methods():
    repository = GeneroRepository()
    use_case = ManterGenero(repository)
    controller = ManterGeneroController(use_case)

    return controller


def atualizar_genero_composer():
    controller = compose_methods()
    return controller.atualizar

def buscar_generos_composer():
    controller = compose_methods()
    return controller.buscar

def buscar_genero_por_id_composer():
    controller = compose_methods()
    return controller.buscar_por_id

def excluir_genero_composer():
    controller = compose_methods()
    return controller.excluir

def cadastrar_genero_composer():
    controller = compose_methods()
    return controller.cadastrar

def atualizar_genero_composer():
    controller = compose_methods()
    return controller.atualizar