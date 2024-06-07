from src.infra.db.config import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from typing import List
from .genero_rpg import genero_rpg_association

class GeneroEntity(Base):
    __tablename__ = "genero"

    id = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String)

    rpgs = relationship("RPGEntity", 
                            secondary = genero_rpg_association,
                            back_populates="generos",
                            lazy="selectin",
                    )
