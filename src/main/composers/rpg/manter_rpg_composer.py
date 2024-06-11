from src.data.use_cases.rpg import ManterRPG
from src.infra.db.repositories import RPGRepository, MestreRepository
from src.presentation.controller.rpg import ManterRPGController

def compose_methods():
    repository = RPGRepository()
    mestre_repository = MestreRepository()
    use_case = ManterRPG(repository, mestre_repository)
    controller = ManterRPGController(use_case)

    return controller


def atualizar_rpg_composer():
    controller = compose_methods()
    return controller.atualizar

def buscar_rpgs_composer():
    controller = compose_methods()
    return controller.buscar

def buscar_rpg_por_id_composer():
    controller = compose_methods()
    return controller.buscar_por_id

def excluir_rpg_composer():
    controller = compose_methods()
    return controller.excluir

def cadastrar_rpg_composer():
    controller = compose_methods()
    return controller.cadastrar

def atualizar_rpg_composer():
    controller = compose_methods()
    return controller.atualizar