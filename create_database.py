from src.infra.db.entities  import *
from src.infra.db.config.db_config import DBConnectionHandler
from src.infra.db.config.db_base import Base
from sqlalchemy import text

conn_db = DBConnectionHandler()

engine = conn_db.get_engine()
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

with engine.connect() as con:
    with open("data.sql") as file:
        try:
            query = text(file.read())
            con.execute(query)
            con.commit()
        except Exception as e:
            print(e)
            con.rollback()
