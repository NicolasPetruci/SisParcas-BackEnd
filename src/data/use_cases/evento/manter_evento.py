from src.domain.models import Evento
from src.domain.use_cases.evento import ManterEventoInterface
from src.data.interfaces import EventoRepositoryInterface
from src.errors import HttpError
from typing import Dict, List

class ManterEvento(ManterEventoInterface):

    @classmethod
    def __init__(self, repository: EventoRepositoryInterface):
        self.__repository = repository

    
    @classmethod
    def buscar_evento_por_id(self, id: int) -> Dict:
        evento = self.__repository.find_by_id(id)
        if evento is None:
            raise HttpError(HttpError.error_404("Evento não encontrado."))
        return evento.to_json()

    @classmethod
    def cadastrar(self, evento: Evento)->Dict:
        novo_evento: Evento = Evento(
            None, 
            evento.nome,
            evento.descricao,
            evento.local,
            evento.online,
            evento.data_hora,
            evento.tipo_evento,
            evento.participantes,
            )
        return {
            "evento": self.__repository.insert(novo_evento).to_json(),
            "message": "Evento cadastrado com sucesso.",
        }
    

    @classmethod
    def buscar_eventos(self) -> List[Dict]:
        eventos: List[Evento] = self.__repository.find_all()
        return list(c.to_json() for c in eventos) 
    
    @classmethod
    def atualizar(self, evento: Evento) -> Dict:
        evento_atualizado = self.__repository.update(evento)
        if evento_atualizado is None:
            raise HttpError(HttpError.error_404("Evento não encontrado."))
        return {
            "evento": evento_atualizado.to_json(),
            "message": "Evento cadastrado com sucesso.",
        }
    
    @classmethod
    def excluir(self, id: int) -> Dict: 
        evento_excluido = self.__repository.delete_by_id(id)
        if evento_excluido is None:
            raise HttpError(HttpError.error_404("Evento não encontrado."))
        return {
            "evento": evento_excluido.to_json(),
            "message": "Evento cadastrado com sucesso.",
        }