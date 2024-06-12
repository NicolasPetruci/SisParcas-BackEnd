from src.data.use_cases.sessao import BuscarSessoesRPG
from src.infra.db.repositories import SessaoRepository
from src.presentation.controller.sessao import BuscarSessoesRPGController

def compose_methods():
    repository = SessaoRepository()
    use_case = BuscarSessoesRPG(repository)
    controller = BuscarSessoesRPGController(use_case)

    return controller


def buscar_por_id_rpg_composer():
    controller = compose_methods()
    return controller.buscar_por_id_rpg