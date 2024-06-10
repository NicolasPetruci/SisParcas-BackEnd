from src.data.use_cases.usuario import BuscarCargosUsuario
from src.infra.db.repositories import UsuarioRepository
from src.presentation.controller.usuario import BuscarCargosUsuarioController

def buscar_cargos_usuario_composer():
    repository = UsuarioRepository()
    use_case = BuscarCargosUsuario(repository)
    controller = BuscarCargosUsuarioController(use_case)

    return controller.buscar_cargos_usuario
