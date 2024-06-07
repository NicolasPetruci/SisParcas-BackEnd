from src.domain.models import Genero
from src.infra.db.entities import GeneroEntity
from src.infra.db.config import DBConnectionHandler
from src.data.interfaces import GeneroRepositoryInterface
from typing import List

class GeneroRepository(GeneroRepositoryInterface):

    @classmethod
    def insert(cls, genero: Genero) -> Genero:
        with DBConnectionHandler() as database:
            try: 
                entity = GeneroEntity(
                    descricao = genero.descricao
                )
                database.session.add(entity)
                database.session.commit()
                return Genero(entity.id, entity.descricao)
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def find_all(cls)->List[Genero]:
        with DBConnectionHandler() as database:
            try:
                generos = (
                    Genero(entity.id, entity.descricao) 
                    for entity in 
                    database.session
                        .query(GeneroEntity)
                        .all()
                )
                return generos
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def delete_by_id(cls, id: int) -> Genero:
        with DBConnectionHandler() as database:
            try:
                entity = database.session.get(GeneroEntity, id)
                if entity is None:
                    return None
                database.session.delete(entity)
                database.session.commit()
                return Genero(entity.id, entity.descricao)
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def find_by_id(cls, id: int) -> Genero:
        with DBConnectionHandler() as database:
            try:
                entity = (
                    database.session.get(GeneroEntity, id)
                )
                if entity is None:
                    return None
                return Genero(entity.id, entity.descricao)
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def update(cls, genero: Genero) -> Genero:
        with DBConnectionHandler() as database:
            try:
                entity = database.session.get(GeneroEntity, genero.id)
                if entity is None:
                    return None
                entity.descricao = genero.descricao
                database.session.commit()
                return Genero(entity.id, entity.descricao)
            except Exception as exception:
                database.session.rollback()
                raise exception
