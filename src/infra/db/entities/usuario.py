from src.infra.db.config import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column 
from datetime import date

class UsuarioEntity(Base):

    __tablename__ = "usuario"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    email: Mapped[str]
    telefone: Mapped[str]
    senha: Mapped[str]
    aniversario: Mapped[date]
    id_cargo: Mapped[int] = mapped_column(ForeignKey("cargo.id"))
    cargo: Mapped["CargoEntity"] = relationship(back_populates="usuarios")
  