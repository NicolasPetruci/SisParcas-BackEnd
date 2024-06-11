from src.domain.use_cases.evento import ListarParticipantesInterface
from src.domain.models import Evento, Usuario
from src.data.interfaces import EventoRepositoryInterface
from src.errors import HttpError
from typing import List, Dict

class ListarParticipantes(ListarParticipantesInterface):

    @classmethod
    def __init__(self, repository: EventoRepositoryInterface):
        self.__repository = repository

    @classmethod
    def buscar_participantes_por_id_evento(self, id: int) -> List[Dict]: 
        evento: Evento = self.__repository.find_by_id(id)
        if evento is None:
            raise HttpError(HttpError.error_404("Evento não encontrado."))
        if not evento.participantes:
            raise HttpError(HttpError.error_400("Evento não possui participantes."))
        return [
                self.participante_relatorio_to_json(index, participante) 
                for index, participante in enumerate(evento.participantes, start=1)
               ]

    @classmethod
    def participante_relatorio_to_json(self, index: int, participante: Usuario):
        return {
            "numero": index,
            "nome": participante.nome,
            "telefone": participante.telefone,
        }