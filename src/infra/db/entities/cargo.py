from src.infra.db.config import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from typing import List
from .usuario_cargo import usuario_cargo_association

class CargoEntity(Base):
    __tablename__ = "cargo"

    id = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String)

    usuarios = relationship("UsuarioEntity",
                            secondary=usuario_cargo_association,
                            back_populates="cargos")
