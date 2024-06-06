from src.infra.db.config import Base
from sqlalchemy import Table, Column, Integer, ForeignKey

jogador_sessao_association = Table(
    "jogador_sessao",
    Base.metadata,
    Column("id_sessao", Integer, ForeignKey("sessao.id")),
    Column("id_usuario", Integer, ForeignKey("usuario.id"))
)