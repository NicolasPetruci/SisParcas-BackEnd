from src.infra.db.config import Base
from sqlalchemy import Table, Column, Integer, ForeignKey

participante_evento_association = Table(
    "participante_evento",
    Base.metadata,
    Column("id_evento", Integer, ForeignKey("evento.id")),
    Column("id_usuario", Integer, ForeignKey("usuario.id"))
)