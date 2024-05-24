from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from decouple import config

class DBConnectionHandler:
    
    def __init__(self)->None:
        self.conn_string = "postgresql://postgres:123@localhost:5432/sisparcas"
        self.session = None
    
    def get_engine(self):   
        engine = create_engine(self.conn_string)
        return engine
    
    def __enter__(self):
        engine = self.get_engine()
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()