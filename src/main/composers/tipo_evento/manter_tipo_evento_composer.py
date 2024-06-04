from src.data.use_cases.tipo_evento import ManterTipoEvento
from src.infra.db.repositories import TipoEventoRepository
from src.presentation.controller.tipo_evento import ManterTipoEventoController

def compose_methods():
    repository = TipoEventoRepository()
    use_case = ManterTipoEvento(repository)
    controller = ManterTipoEventoController(use_case)

    return controller


def atualizar_tipo_evento_composer():
    controller = compose_methods()
    return controller.atualizar

def buscar_tipo_eventos_composer():
    controller = compose_methods()
    return controller.buscar

def buscar_tipo_evento_por_id_composer():
    controller = compose_methods()
    return controller.buscar_por_id

def excluir_tipo_evento_composer():
    controller = compose_methods()
    return controller.excluir

def cadastrar_tipo_evento_composer():
    controller = compose_methods()
    return controller.cadastrar

def atualizar_tipo_evento_composer():
    controller = compose_methods()
    return controller.atualizar