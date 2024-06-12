from src.data.use_cases.mestre import ManterMestre
from src.infra.db.repositories import MestreRepository
from src.presentation.controller.mestre import BuscarMestreLogadoController

def compose_methods():
    repository = MestreRepository()
    use_case = ManterMestre(repository)
    controller = BuscarMestreLogadoController(use_case)

    return controller

def buscar_mestre_logado_composer():
    controller = compose_methods()
    return controller.buscar_mestre_logado