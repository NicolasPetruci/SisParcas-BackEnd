from src.data.use_cases.evento import VisualizarEventos
from src.infra.db.repositories import EventoRepository
from src.presentation.controller.evento import VisualizarEventosController

def compose_methods():
    repository = EventoRepository()
    use_case = VisualizarEventos(repository)
    controller = VisualizarEventosController(use_case)

    return controller

def visualizar_eventos_composer():
    controller = compose_methods()
    return controller.visualizar_eventos

