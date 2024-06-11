from src.domain.models import Evento
from src.infra.db.entities import EventoEntity, TipoEventoEntity, UsuarioEntity
from src.infra.db.config import DBConnectionHandler
from src.data.interfaces import EventoRepositoryInterface
from sqlalchemy import select
from typing import List
from datetime import datetime
class EventoRepository(EventoRepositoryInterface):

    @classmethod
    def insert(cls, evento: Evento) -> Evento:
        with DBConnectionHandler() as database:
            try: 
                entity = EventoEntity(
                    nome = evento.nome,
                    descricao = evento.descricao,
                    local = evento.local,
                    online = evento.online,
                    data_hora = evento.data_hora,
                    tipo_evento = database.session.get(TipoEventoEntity, evento.tipo_evento.id),
                    participantes = [
                         database.session.get(UsuarioEntity, usuario.id) 
                         for usuario in evento.participantes
                    ]
                )
                database.session.add(entity)
                database.session.commit()
                return Evento.from_entity(entity)
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def find_all(cls)->List[Evento]:
        with DBConnectionHandler() as database:
            try:
                eventos = (
                    Evento.from_entity(entity)
                    for entity in 
                    database.session.scalars(
                                select(EventoEntity)
                            ).all()
                )
                return eventos
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def delete_by_id(cls, id: int) -> Evento:
        with DBConnectionHandler() as database:
            try:
                entity = database.session.get(EventoEntity, id)
                if entity is None:
                    return None
                database.session.delete(entity)
                database.session.commit()
                return Evento.from_entity(entity)
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def find_by_id(cls, id: int) -> Evento:
        with DBConnectionHandler() as database:
            try:
                entity = (
                    database.session.get(EventoEntity, id)
                )
                if entity is None:
                    return None
                return Evento.from_entity(entity)
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def update(cls, evento: Evento) -> Evento:
        with DBConnectionHandler() as database:
            try:
                entity: EventoEntity = database.session.get(EventoEntity, evento.id)
                if entity is None:
                    return None
                if evento.nome:
                    entity.nome = evento.nome
                if evento.descricao:
                    entity.descricao = evento.descricao
                if evento.local:
                    entity.local = evento.local
                if evento.online:
                    entity.online = evento.online
                if evento.tipo_evento:
                    entity.tipo_evento = database.session.get(TipoEventoEntity, evento.tipo_evento.id)
                if evento.participantes:
                    entity.participantes = [
                         database.session.get(UsuarioEntity, usuario.id) 
                         for usuario in evento.participantes
                    ]
                database.session.commit()
                return Evento.from_entity(entity)
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def find_all_between_dates(cls, data_inicial: datetime, data_final: datetime) -> List[Evento]:
        with DBConnectionHandler() as database:
            try:
                eventos = (
                    Evento.from_entity(entity)
                    for entity in 
                    database.session.scalars(
                                select(EventoEntity)
                                .filter(EventoEntity.data_hora.between(data_inicial, data_final))
                            ).all()
                )
                return eventos
            except Exception as exception:
                database.session.rollback()
                raise exception