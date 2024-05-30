from src.data.use_cases.usuario import Login
from src.infra.db.repositories import CargoRepository
from src.presentation.controller.usuario import LoginController

def compose_methods():
    repository = UsuarioRepository()
    use_case = Login(repository)
    controller = LoginController(use_case)

    return controller


def login_composer():
    controller = compose_methods()
    return controller.login
