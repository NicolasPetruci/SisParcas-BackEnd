from src.domain.models import Cargo
from src.infra.db.entities import Cargo as CargoEntity
from src.infra.db.config import DBConnectionHandler
from src.data.interfaces import CargoRepositoryInterface

class CargoRepository(CargoRepositoryInterface):

    @classmethod
    def insert(cls, cargo: Cargo)->Cargo:
        with DBConnectionHandler() as database:
            try: 
                novo_cargo = CargoEntity(
                    descricao = cargo.descricao
                )
                database.session.add(novo_cargo)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception