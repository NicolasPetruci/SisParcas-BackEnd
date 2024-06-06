from src.infra.db.config import Base
from sqlalchemy import Table, Column, Integer, ForeignKey

jogador_rpg_association = Table(
    "jogador_rpg",
    Base.metadata,
    Column("id_rpg", Integer, ForeignKey("rpg.id")),
    Column("id_usuario", Integer, ForeignKey("usuario.id"))
)