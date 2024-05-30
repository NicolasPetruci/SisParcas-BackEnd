from src.infra.db.config import Base
from sqlalchemy.orm import relationship, mapped_column, Mapped
from typing import List

class CargoEntity(Base):
    __tablename__ = "cargo"

    id: Mapped[int] = mapped_column(primary_key=True)
    descricao: Mapped[str]

    usuarios: Mapped[List["UsuarioEntity"]] = relationship(back_populates="cargo")
