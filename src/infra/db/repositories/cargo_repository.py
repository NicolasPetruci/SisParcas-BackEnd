from src.domain.models import Cargo
from src.infra.db.entities import CargoEntity
from src.infra.db.config import DBConnectionHandler
from src.data.interfaces import CargoRepositoryInterface
from typing import List

class CargoRepository(CargoRepositoryInterface):

    @classmethod
    def insert(cls, cargo: Cargo) -> Cargo:
        with DBConnectionHandler() as database:
            try: 
                entity = CargoEntity(
                    descricao = cargo.descricao
                )
                database.session.add(entity)
                database.session.commit()
                return Cargo(entity.id, entity.descricao)
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def find_all(cls)->List[Cargo]:
        with DBConnectionHandler() as database:
            try:
                cargos = (
                    Cargo(entity.id, entity.descricao) 
                    for entity in 
                    database.session
                        .query(CargoEntity)
                        .all()
                )
                return cargos
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def delete_by_id(cls, id: int) -> Cargo:
        with DBConnectionHandler() as database:
            try:
                entity = database.session.get(CargoEntity, id)
                database.session.delete(entity)
                database.session.commit()
                return Cargo(entity.id, entity.descricao)
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def find_by_id(cls, id: int) -> Cargo:
        with DBConnectionHandler() as database:
            try:
                entity = (
                    database.session.get(CargoEntity, id)
                )
                if entity is None:
                    return None
                return Cargo(entity.id, entity.descricao)
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def update(cls, cargo: Cargo) -> Cargo:
        with DBConnectionHandler() as database:
            try:
                entity = database.session.get(CargoEntity, cargo.id)
                entity.descricao = cargo.descricao
                database.session.commit()
                return Cargo(entity.id, entity.descricao)
            except Exception as exception:
                database.session.rollback()
                raise exception
