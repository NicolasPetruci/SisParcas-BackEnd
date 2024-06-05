from src.data.use_cases.evento import ManterEvento
from src.infra.db.repositories import EventoRepository
from src.presentation.controller.evento import ManterEventoController

def compose_methods():
    repository = EventoRepository()
    use_case = ManterEvento(repository)
    controller = ManterEventoController(use_case)

    return controller


def atualizar_evento_composer():
    controller = compose_methods()
    return controller.atualizar

def buscar_eventos_composer():
    controller = compose_methods()
    return controller.buscar

def buscar_evento_por_id_composer():
    controller = compose_methods()
    return controller.buscar_por_id

def excluir_evento_composer():
    controller = compose_methods()
    return controller.excluir

def cadastrar_evento_composer():
    controller = compose_methods()
    return controller.cadastrar

def atualizar_evento_composer():
    controller = compose_methods()
    return controller.atualizar