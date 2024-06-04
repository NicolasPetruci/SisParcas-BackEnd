from src.infra.db.config import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from typing import List
from .evento import EventoEntity

class TipoEventoEntity(Base):
    __tablename__ = "tipo_evento"

    id = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String)

    usuarios = relationship("EventoEntity", back_populates="tipo_evento")
