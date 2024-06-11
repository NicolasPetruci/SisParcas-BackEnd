from src.data.use_cases.rpg import VisualizarRPGs
from src.infra.db.repositories import RPGRepository
from src.presentation.controller.rpg import VisualizarRPGsController

def compose_methods():
    repository = RPGRepository()
    use_case = VisualizarRPGs(repository)
    controller = VisualizarRPGsController(use_case)

    return controller

def visualizar_rpgs_composer():
    controller = compose_methods()
    return controller.visualizar_rpgs

