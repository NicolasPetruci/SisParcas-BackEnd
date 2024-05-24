from src.infra.db.config import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

class Usuario(Base):

    __tablename__ = "usuario"

    id_usuario = Column(Integer, primary_key=True)
    nome = Column(String)
    telefone = Column(String)
    senha = Column(String)
    aniversario = Column(Date)

    id_cargo = Column(Integer, ForeignKey("cargo.id"))
    cargo = relationship("Cargo", back_populates="cargo")
  