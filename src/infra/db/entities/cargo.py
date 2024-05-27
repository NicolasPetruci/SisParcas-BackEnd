from src.infra.db.config import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class CargoEntity(Base):
    __tablename__ = "cargo"

    id = Column(Integer, primary_key=True)
    descricao = Column(String)

    usuarios = relationship("UsuarioEntity", back_populates="cargo")
