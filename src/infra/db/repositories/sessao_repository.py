from src.domain.models import Sessao
from src.infra.db.entities import SessaoEntity, RPGEntity, UsuarioEntity
from src.infra.db.config import DBConnectionHandler
from src.data.interfaces import SessaoRepositoryInterface
from sqlalchemy import select
from typing import List

class SessaoRepository(SessaoRepositoryInterface):

    @classmethod
    def insert(cls, sessao: Sessao) -> Sessao:
        with DBConnectionHandler() as database:
            try: 
                entity = SessaoEntity(
                    nome = sessao.nome,
                    descricao = sessao.descricao,
                    temporada = sessao.temporada,
                    numero = sessao.numero,
                    data_hora = sessao.data_hora,
                    rpg = database.session.get(RPGEntity, sessao.rpg.id),
                    jogadores = [
                         database.session.get(UsuarioEntity, usuario.id) 
                         for usuario in sessao.jogadores
                    ]
                )
                database.session.add(entity)
                database.session.commit()
                return Sessao.from_entity(entity)
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def find_all(cls)->List[Sessao]:
        with DBConnectionHandler() as database:
            try:
                sessoes = (
                    Sessao.from_entity(entity)
                    for entity in 
                    database.session.scalars(
                                select(SessaoEntity)
                            ).all()
                )
                return sessoes
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def delete_by_id(cls, id: int) -> Sessao:
        with DBConnectionHandler() as database:
            try:
                entity = database.session.get(SessaoEntity, id)
                if entity is None:
                    return None
                database.session.delete(entity)
                database.session.commit()
                return Sessao.from_entity(entity)
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def find_by_id(cls, id: int) -> Sessao:
        with DBConnectionHandler() as database:
            try:
                entity = (
                    database.session.get(SessaoEntity, id)
                )
                if entity is None:
                    return None
                return Sessao.from_entity(entity)
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def update(cls, sessao: Sessao) -> Sessao:
        with DBConnectionHandler() as database:
            try:
                entity: SessaoEntity = database.session.get(SessaoEntity, sessao.id)
                if entity is None:
                    return None
                if sessao.nome:
                    entity.nome = sessao.nome
                if sessao.descricao:
                    entity.descricao = sessao.descricao
                if sessao.temporada:
                    entity.temporada = sessao.temporada
                if sessao.numero:
                    entity.numero = sessao.numero
                if sessao.rpg:
                    entity.rpg = database.session.get(RPGEntity, sessao.rpg.id)
                if sessao.jogadores:
                    entity.jogadores = [
                         database.session.get(UsuarioEntity, usuario.id) 
                         for usuario in sessao.jogadores
                    ]
                database.session.commit()
                return Sessao.from_entity(entity)
            except Exception as exception:
                database.session.rollback()
                raise exception
