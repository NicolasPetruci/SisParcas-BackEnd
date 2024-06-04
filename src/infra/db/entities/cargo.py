from src.infra.db.config import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from typing import List

class CargoEntity(Base):
    __tablename__ = "cargo"

    id = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String)

    usuarios = relationship("UsuarioEntity", back_populates="cargo")
