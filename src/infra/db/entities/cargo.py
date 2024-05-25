from src.infra.db.config import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Cargo(Base):
    __tablename__ = "cargo"

    id_cargo = Column(Integer, primary_key=True)
    descricao = Column(String)

    #usuarios = relationship("Usuario", back_populates="usuarios")
