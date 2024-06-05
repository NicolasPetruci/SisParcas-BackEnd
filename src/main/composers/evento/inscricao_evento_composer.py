from src.data.use_cases.evento import InscricaoEvento
from src.infra.db.repositories import EventoRepository, UsuarioRepository
from src.presentation.controller.evento import InscricaoEventoController

def compose_methods():
    repository = EventoRepository()
    usuario_repository = UsuarioRepository()
    use_case = InscricaoEvento(repository, usuario_repository)
    controller = InscricaoEventoController(use_case)

    return controller

def inscrever_composer():
    controller = compose_methods()
    return controller.inscrever


def desinscrever_composer():
    controller = compose_methods()
    return controller.desinscrever