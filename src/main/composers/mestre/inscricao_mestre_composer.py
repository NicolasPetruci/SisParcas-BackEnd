from src.data.use_cases.mestre import InscricaoMestre
from src.infra.db.repositories import MestreRepository, UsuarioRepository
from src.presentation.controller.mestre import InscricaoMestreController

def compose_methods():
    repository = MestreRepository()
    usuario_repository = UsuarioRepository()
    use_case = InscricaoMestre(repository, usuario_repository)
    controller = InscricaoMestreController(use_case)

    return controller

def deferir_mestre_composer():
    controller = compose_methods()
    return controller.deferir


def indeferir_mestre_composer():
    controller = compose_methods()
    return controller.indeferir