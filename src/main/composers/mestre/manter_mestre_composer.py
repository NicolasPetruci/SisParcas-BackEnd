from src.data.use_cases.mestre import ManterMestre
from src.infra.db.repositories import MestreRepository
from src.presentation.controller.mestre import ManterMestreController

def compose_methods():
    repository = MestreRepository()
    use_case = ManterMestre(repository)
    controller = ManterMestreController(use_case)

    return controller


def atualizar_mestre_composer():
    controller = compose_methods()
    return controller.atualizar

def buscar_mestres_composer():
    controller = compose_methods()
    return controller.buscar

def buscar_mestre_por_id_composer():
    controller = compose_methods()
    return controller.buscar_por_id

def excluir_mestre_composer():
    controller = compose_methods()
    return controller.excluir

def cadastrar_mestre_composer():
    controller = compose_methods()
    return controller.cadastrar

def atualizar_mestre_composer():
    controller = compose_methods()
    return controller.atualizar