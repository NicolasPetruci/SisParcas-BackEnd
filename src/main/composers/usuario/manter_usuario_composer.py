from src.data.use_cases.usuario import ManterUsuario
from src.infra.db.repositories import UsuarioRepository
from src.presentation.controller.usuario import ManterUsuarioController

def compose_methods():
    repository = UsuarioRepository()
    use_case = ManterUsuario(repository)
    controller = ManterUsuarioController(use_case)

    return controller


def atualizar_usuario_composer():
    controller = compose_methods()
    return controller.atualizar

def buscar_usuarios_composer():
    controller = compose_methods()
    return controller.buscar

def buscar_usuario_por_id_composer():
    controller = compose_methods()
    return controller.buscar_por_id

def excluir_usuario_composer():
    controller = compose_methods()
    return controller.excluir

def cadastrar_usuario_composer():
    controller = compose_methods()
    return controller.cadastrar

def atualizar_usuario_composer():
    controller = compose_methods()
    return controller.atualizar