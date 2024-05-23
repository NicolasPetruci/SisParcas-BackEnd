from src.main.db.config import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Cargo(Base):
    __tablename__ = "cargo"

    id_cargo = Column(Integer, primary_key=True)
    descricao = Column(String)

    usuarios = relationship("Produtos", back_populates="cargo")
