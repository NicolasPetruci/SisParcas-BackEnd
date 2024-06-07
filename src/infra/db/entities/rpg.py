from src.infra.db.config import Base
from sqlalchemy import ForeignKey, Column, Integer, Date, String, Boolean
from sqlalchemy.orm import relationship
from datetime import date
from .usuario import UsuarioEntity
from .jogador_rpg import jogador_rpg_association
from .genero_rpg import genero_rpg_association

class RPGEntity(Base):

    __tablename__ = "rpg"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    descricao = Column(String)

    id_mestre = Column(Integer, ForeignKey("mestre.id"))
    mestre = relationship("MestreEntity", back_populates="rpgs", lazy="joined")
    jogadores = relationship(
                                "UsuarioEntity", 
                                secondary = jogador_rpg_association,
                                back_populates="rpgs",
                                lazy="selectin"
                    )
    generos = relationship(
                            "GeneroEntity", 
                            secondary = genero_rpg_association,
                            back_populates="rpgs",
                            lazy="selectin"
                    )
  