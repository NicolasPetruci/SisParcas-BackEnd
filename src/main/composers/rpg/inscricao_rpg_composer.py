from src.data.use_cases.rpg import InscricaoRPG
from src.infra.db.repositories import RPGRepository, UsuarioRepository
from src.presentation.controller.rpg import InscricaoRPGController

def compose_methods():
    repository = RPGRepository()
    usuario_repository = UsuarioRepository()
    use_case = InscricaoRPG(repository, usuario_repository)
    controller = InscricaoRPGController(use_case)

    return controller

def inscrever_composer():
    controller = compose_methods()
    return controller.inscrever


def desinscrever_composer():
    controller = compose_methods()
    return controller.desinscrever