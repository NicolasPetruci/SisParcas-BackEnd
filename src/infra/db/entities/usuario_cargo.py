from src.infra.db.config import Base
from sqlalchemy import Table, Column, Integer, ForeignKey

usuario_cargo_association = Table(
    "usuario_cargo",
    Base.metadata,
    Column("id_cargo", Integer, ForeignKey("cargo.id")),
    Column("id_usuario", Integer, ForeignKey("usuario.id"))
)