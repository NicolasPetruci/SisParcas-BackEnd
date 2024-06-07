from src.infra.db.config import Base
from sqlalchemy import ForeignKey, Column, Integer, Date, String, Boolean
from sqlalchemy.orm import relationship, backref
from datetime import date
from .usuario import UsuarioEntity

class MestreEntity(Base):

    __tablename__ = "mestre"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ativo = Column(Boolean)
    id_usuario = Column(Integer, ForeignKey("usuario.id"))
    usuario = relationship(
                            "UsuarioEntity",
                            backref=backref("mestre", cascade="all,delete", uselist=False)
                    )
    rpgs = relationship(
                        "RPGEntity", 
                        back_populates="mestre",
                        lazy="selectin"
                )
  