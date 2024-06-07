from src.infra.db.config import Base
from sqlalchemy import ForeignKey, Column, Integer, Date, String, Boolean
from sqlalchemy.orm import relationship
from datetime import date
from .usuario import UsuarioEntity

class MestreEntity(Base):

    __tablename__ = "rpg"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ativo = Column(Boolean)
    id_usuario = Column(Integer, ForeignKey("usuario.id"))
    usuario = relationship("MestreEntity", uselist=False, backref="mestre", lazy="joined")
    rpgs = relationship(
                        "RpgEntity", 
                        back_populates="mestre",
                        lazy="selectin"
                )
  