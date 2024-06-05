from src.infra.db.config import Base
from sqlalchemy import ForeignKey, Column, Integer, Date, String
from sqlalchemy.orm import relationship
from datetime import date
from .cargo import CargoEntity
from .participante_evento import participante_evento_association

class UsuarioEntity(Base):

    __tablename__ = "usuario"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    email = Column(String)
    telefone = Column(String)
    senha = Column(String)
    aniversario = Column(Date)

    id_cargo = Column(Integer, ForeignKey("cargo.id"))
    cargo = relationship("CargoEntity", back_populates="usuarios", lazy="joined")
    eventos = relationship("EventoEntity", 
                            secondary = participante_evento_association,
                            back_populates="participantes",
                )
  