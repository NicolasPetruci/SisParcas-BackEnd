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
                novo_cargo = CargoEntity(
                    descricao = cargo.descricao
                )
                database.session.add(novo_cargo)
                database.session.commit()
                return Cargo(novo_cargo.id_cargo, novo_cargo.descricao)
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def find_all(cls)->List[Cargo]:
        with DBConnectionHandler() as database:
            try:
                cargos = (
                    Cargo(entity.id_cargo, entity.descricao) 
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
    def delete_by_id(cls, id) -> Cargo: pass

    @classmethod
    def find_by_id(cls, id) -> Cargo: pass