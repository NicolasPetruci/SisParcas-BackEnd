from src.infra.db.config import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from typing import List

class GeneroEntity(Base):
    __tablename__ = "genero"

    id = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String)

    rpgs = relationship("RpgEntity", back_populates="genero")
