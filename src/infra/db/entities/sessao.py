from src.infra.db.config import Base
from sqlalchemy import ForeignKey, Column, Integer, DateTime, String, Boolean
from sqlalchemy.orm import relationship
from datetime import date
from .usuario import UsuarioEntity
from .jogador_sessao import jogador_sessao_association

class SessaoEntity(Base):

    __tablename__ = "sessao"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    descricao = Column(String)
    data_hora = Column(DateTime)
    temporada = Column(Integer)
    numero_sessao = Column(Integer)
    
    id_rpg = Column(Integer, ForeignKey("rpg.id"))
    rpg = relationship("RpgEntity", back_populates="sessoes", lazy="joined")
    jogadores = relationship(
                                "UsuarioEntity", 
                                secondary = jogador_sessao_association,
                                back_populates="sessoes",
                                lazy="selectin"
                    )
  