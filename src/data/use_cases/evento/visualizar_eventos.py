from src.domain.use_cases.evento import VisualizarEventosInterface
from src.domain.models import Evento, Usuario
from src.data.interfaces import EventoRepositoryInterface
from src.errors import HttpError
from typing import List, Dict
from datetime import datetime

class VisualizarEventos(VisualizarEventosInterface):

    @classmethod
    def __init__(self, repository: EventoRepositoryInterface):
        self.__repository = repository

    @classmethod
    def visualizar_eventos(self, data_inicial: datetime, data_final: datetime) -> List[Dict]: 
        eventos: List[Evento] = self.__repository.find_all_between_dates(data_inicial, data_final)
        if eventos is None:
            raise HttpError(HttpError.error_404("Evento não encontrado."))
        return [
                self.evento_relatorio_to_json(index, evento) 
                for index, evento in enumerate(eventos, start=1)
               ]

    @classmethod
    def evento_relatorio_to_json(self, index: int, evento: Evento):
        return {
            "numero": index,
            "nome": evento.nome,
            "local": evento.local,
            "tipo_evento": evento.tipo_evento.descricao,
            "data": f"{evento.data_hora.day}/{evento.data_hora.month}/{evento.data_hora.year}, {evento.data_hora.hour:02}:{evento.data_hora.minute:02}",
            "presencial": "Não" if evento.online else "Sim",
            "numero_inscritos": len(evento.participantes) 
        }