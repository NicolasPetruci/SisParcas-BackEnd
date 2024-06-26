from src.infra.db.config import Base
from sqlalchemy import ForeignKey, Column, Integer, Date, String
from sqlalchemy.orm import relationship, backref
from datetime import date
from .cargo import CargoEntity
from .participante_evento import participante_evento_association
from .jogador_rpg import jogador_rpg_association
from .jogador_sessao import jogador_sessao_association
from .usuario_cargo import usuario_cargo_association

class UsuarioEntity(Base):

    __tablename__ = "usuario"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    email = Column(String)
    telefone = Column(String)
    senha = Column(String)
    aniversario = Column(Date)

    cargos = relationship("CargoEntity", 
                            secondary = usuario_cargo_association,
                            back_populates="usuarios",
                            lazy="selectin"
                )
    eventos = relationship("EventoEntity", 
                            secondary = participante_evento_association,
                            back_populates="participantes",
                )
    rpgs = relationship("RPGEntity", 
                        secondary = jogador_rpg_association,
                        back_populates="jogadores",
                )
  
    sessoes = relationship("SessaoEntity", 
                        secondary = jogador_sessao_association,
                        back_populates="jogadores",
                )