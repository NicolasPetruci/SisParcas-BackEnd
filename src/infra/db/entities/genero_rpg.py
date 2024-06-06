from src.infra.db.config import Base
from sqlalchemy import Table, Column, Integer, ForeignKey

genero_rpg_association = Table(
    "genero_rpg",
    Base.metadata,
    Column("id_rpg", Integer, ForeignKey("rpg.id")),
    Column("id_genero", Integer, ForeignKey("genero.id"))
)