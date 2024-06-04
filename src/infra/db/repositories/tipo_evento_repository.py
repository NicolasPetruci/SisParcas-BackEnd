from src.domain.models import TipoEvento
from src.infra.db.entities import TipoEventoEntity
from src.infra.db.config import DBConnectionHandler
from src.data.interfaces import TipoEventoRepositoryInterface
from typing import List

class TipoEventoRepository(TipoEventoRepositoryInterface):

    @classmethod
    def insert(cls, tipo_evento: TipoEvento) -> TipoEvento:
        with DBConnectionHandler() as database:
            try: 
                entity = TipoEventoEntity(
                    descricao = tipo_evento.descricao
                )
                database.session.add(entity)
                database.session.commit()
                return TipoEvento(entity.id, entity.descricao)
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def find_all(cls)->List[TipoEvento]:
        with DBConnectionHandler() as database:
            try:
                tipo_eventos = (
                    TipoEvento(entity.id, entity.descricao) 
                    for entity in 
                    database.session
                        .query(TipoEventoEntity)
                        .all()
                )
                return tipo_eventos
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def delete_by_id(cls, id: int) -> TipoEvento:
        with DBConnectionHandler() as database:
            try:
                entity = database.session.get(TipoEventoEntity, id)
                if entity is None:
                    return None
                database.session.delete(entity)
                database.session.commit()
                return TipoEvento(entity.id, entity.descricao)
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def find_by_id(cls, id: int) -> TipoEvento:
        with DBConnectionHandler() as database:
            try:
                entity = (
                    database.session.get(TipoEventoEntity, id)
                )
                if entity is None:
                    return None
                return TipoEvento(entity.id, entity.descricao)
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def update(cls, tipo_evento: TipoEvento) -> TipoEvento:
        with DBConnectionHandler() as database:
            try:
                entity = database.session.get(TipoEventoEntity, tipo_evento.id)
                if entity is None:
                    return None
                entity.descricao = tipo_evento.descricao
                database.session.commit()
                return TipoEvento(entity.id, entity.descricao)
            except Exception as exception:
                database.session.rollback()
                raise exception
