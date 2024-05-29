from src.infra.db.config import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

class UsuarioEntity(Base):

    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    email = Column(String)
    telefone = Column(String)
    senha = Column(String)
    aniversario = Column(Date)

    id_cargo = Column(Integer, ForeignKey("cargo.id"))
    cargo = relationship("CargoEntity", back_populates="usuarios")
  