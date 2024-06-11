from src.data.use_cases.evento import ListarParticipantes
from src.infra.db.repositories import EventoRepository
from src.presentation.controller.evento import ListarParticipantesController

def compose_methods():
    repository = EventoRepository()
    use_case = ListarParticipantes(repository)
    controller = ListarParticipantesController(use_case)

    return controller

def listar_participantes_composer():
    controller = compose_methods()
    return controller.listar_participantes

