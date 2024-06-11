from src.data.use_cases.usuario import ManterUsuario
from src.infra.db.repositories import UsuarioRepository
from src.presentation.controller.usuario import BuscarUsuarioLogadoController

def compose_methods():
    repository = UsuarioRepository()
    use_case = ManterUsuario(repository)
    controller = BuscarUsuarioLogadoController(use_case)

    return controller


def buscar_usuario_logado_composer():
    controller = compose_methods()
    return controller.buscar_usuario_logado