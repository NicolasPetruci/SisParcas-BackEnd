from typing import List

from src.data.interfaces.mestre_repository import MestreRepositoryInterface
from src.domain.models import Mestre
from src.infra.db.config import DBConnectionHandler
from src.infra.db.entities import MestreEntity, UsuarioEntity, RPGEntity
from sqlalchemy import select

class MestreRepository(MestreRepositoryInterface):

    @classmethod
    def insert(cls, mestre: Mestre) -> Mestre:
        with DBConnectionHandler() as database:
            try:
                entity = MestreEntity(
                    ativo=mestre.ativo,
                    usuario=database.session.get(UsuarioEntity, mestre.usuario.id),
                )
                database.session.add(entity)
                database.session.commit()
                return Mestre.from_entity(entity)
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def find_all(cls) -> List[Mestre]:
        with DBConnectionHandler() as database:
            try:
                entities = database.session.scalars(select(MestreEntity)).all()
                return [Mestre.from_entity(entity) for entity in entities]
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def find_by_id(cls, id: int) -> Mestre:
        with DBConnectionHandler() as database:
            try:
                entity = database.session.get(MestreEntity, id)
                if entity is None:
                    return None
                return Mestre.from_entity(entity)
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def update(cls, mestre: Mestre) -> Mestre:
        with DBConnectionHandler() as database:
            try:
                entity: MestreEntity = database.session.get(MestreEntity, mestre.id)
                if not entity:
                    return None
                if mestre.ativo is not None:
                    entity.ativo = mestre.ativo
                if mestre.usuario is not None:
                    entity.usuario = database.session.get(UsuarioEntity, mestre.usuario.id)
                database.session.commit()
                return Mestre.from_entity(entity)
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def delete_by_id(cls, id: int) -> Mestre:
        with DBConnectionHandler() as database:
            try:
                entity: MestreEntity = database.session.get(MestreEntity, id)
                if not entity:
                    return None
                database.session.delete(entity)
                database.session.commit()
                return Mestre.from_entity(entity)
            except Exception as exception:
                database.session.rollback()
                raise exception
            
    @classmethod
    def find_by_id_usuario(cls, id_usuario: int) -> Mestre:
        with DBConnectionHandler() as database:
            try:
                entity: MestreEntity = database.session.scalars(
                    select(MestreEntity)
                    .filter_by(id_usaurio = id_usuario)
                    .limit(1)
                ).first()
                if entity is None:
                    return None
                return Mestre.from_entity(entity)
            except Exception as exception:
                database.session.rollback()
                raise exception