from src.data.use_cases.rpg import ListarJogadores
from src.infra.db.repositories import RPGRepository
from src.presentation.controller.rpg import ListarJogadoresController

def compose_methods():
    repository = RPGRepository()
    use_case = ListarJogadores(repository)
    controller = ListarJogadoresController(use_case)

    return controller

def listar_jogadores_composer():
    controller = compose_methods()
    return controller.listar_jogadores

