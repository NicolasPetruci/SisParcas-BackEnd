from src.domain.models import Evento, Usuario
from src.domain.use_cases.evento import InscricaoEventoInterface
from src.data.interfaces import EventoRepositoryInterface, UsuarioRepositoryInterface
from src.errors import HttpError
from typing import Dict, List

class InscricaoEvento(InscricaoEventoInterface):

    @classmethod
    def __init__(
            self,
            repository: EventoRepositoryInterface,
            usuario_repository: UsuarioRepositoryInterface 
            ):
        self.__repository = repository
        self.__usuario_repository = usuario_repository
    
    @classmethod
    def inscrever(self, id_usuario: int, id_evento: int) -> Dict:
        evento: Evento = self.__repository.find_by_id(id_evento)
        if evento is None:
            raise HttpError(HttpError.error_404("Evento não encontrado."))
        usuario: Usuario = self.__usuario_repository.find_by_id(id_usuario)
        if usuario is None:
            raise HttpError(HttpError.error_404("Usuario não encontrado."))
        if usuario.id in [participante.id for participante in evento.participantes]:
            raise HttpError(HttpError.error_400("Participante já inscrito."))
        evento.adicionar_participante(usuario)
        evento_atualizado = self.__repository.update(evento)
        return {
            "evento": evento_atualizado.to_json(),
            "message": "Inscrição realizada com sucesso.",
        }

    @classmethod
    def desinscrever(self, id_usuario: int, id_evento: int) -> Dict:
        evento: Evento = self.__repository.find_by_id(id_evento)
        if evento is None:
            raise HttpError(HttpError.error_404("Evento não encontrado."))
        usuario: Usuario = self.__usuario_repository.find_by_id(id_usuario)
        if usuario is None:
            raise HttpError(HttpError.error_404("Usuario não encontrado."))
        if usuario.id not in [participante.id for participante in evento.participantes]:
            raise HttpError(HttpError.error_400("Participante não está inscrito."))
        evento.remover_participante(usuario)
        evento_atualizado = self.__repository.update(evento)
        return {
            "evento": evento_atualizado.to_json(),
            "message": "Inscrição cancelada com sucesso.",
        }