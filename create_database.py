from src.usuario.entity import *
from src.cargo.entity  import *
from src.infra.db.config.db_config import DBConnectionHandler
from src.infra.db.config.db_base import Base

conn_db = DBConnectionHandler()

engine = conn_db.get_engine()

Base.metadata.create_all(engine)