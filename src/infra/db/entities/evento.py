from src.infra.db.config import Base
from sqlalchemy import ForeignKey, Column, Integer, Date, String, Boolean
from sqlalchemy.orm import relationship
from datetime import date
from .tipo_evento import TipoEventoEntity
from .participante_evento import participante_evento_association

class EventoEntity(Base):

    __tablename__ = "evento"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    descricao = Column(String)
    local = Column(String)
    online = Column(Boolean)
    data_hora = Column(Date)

    id_tipo_evento = Column(Integer, ForeignKey("tipo_evento.id"))
    tipo_evento = relationship("TipoEventoEntity", back_populates="eventos")
    participantes = relationship(
                                 "UsuarioEntity", 
                                 secondary = participante_evento_association,
                                 back_populates="eventos",
                    )
  