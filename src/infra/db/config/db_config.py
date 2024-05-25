from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from decouple import config

class DBConnectionHandler:
    
    def __init__(self)->None:
        self.conn_string = "postgresql://postgres:123@localhost:5432/sisparcas"
        self.__engine = self.get_engine()
        self.session = None
    
    def get_engine(self):   
        engine = create_engine(self.conn_string)
        return engine
    
    def __enter__(self):
        session_maker = sessionmaker(bind=self.__engine)
        self.session = session_maker()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()