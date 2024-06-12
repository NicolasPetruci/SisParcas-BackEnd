from src.domain.models import RPG
from src.infra.db.entities import RPGEntity, UsuarioEntity, GeneroEntity, MestreEntity
from src.infra.db.config import DBConnectionHandler
from src.data.interfaces import RPGRepositoryInterface
from sqlalchemy import select
from typing import List

class RPGRepository(RPGRepositoryInterface):

    @classmethod
    def insert(cls, rpg: RPG) -> RPG:
        with DBConnectionHandler() as database:
            try: 
                entity = RPGEntity(
                    nome = rpg.nome,
                    descricao = rpg.descricao,
                    mestre = database.session.get(MestreEntity, rpg.mestre.id),
                    jogadores = [
                         database.session.get(UsuarioEntity, usuario.id) 
                         for usuario in rpg.jogadores
                    ],
                    generos = [
                        database.session.get(GeneroEntity, genero.id) 
                         for genero in rpg.generos
                    ]
                )
                database.session.add(entity)
                database.session.commit()
                return RPG.from_entity(entity)
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def find_all(cls)->List[RPG]:
        with DBConnectionHandler() as database:
            try:
                rpgs = (
                    RPG.from_entity(entity)
                    for entity in 
                    database.session.scalars(
                                select(RPGEntity)
                            ).all()
                )
                return rpgs
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def delete_by_id(cls, id: int) -> RPG:
        with DBConnectionHandler() as database:
            try:
                entity = database.session.get(RPGEntity, id)
                if entity is None:
                    return None
                database.session.delete(entity)
                database.session.commit()
                return RPG.from_entity(entity)
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def find_by_id(cls, id: int) -> RPG:
        with DBConnectionHandler() as database:
            try:
                entity = (
                    database.session.get(RPGEntity, id)
                )
                if entity is None:
                    return None
                return RPG.from_entity(entity)
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def update(cls, rpg: RPG) -> RPG:
        with DBConnectionHandler() as database:
            try:
                entity: RPGEntity = database.session.get(RPGEntity, rpg.id)
                if entity is None:
                    return None
                if rpg.nome:
                    entity.nome = rpg.nome
                if rpg.descricao:
                    entity.descricao = rpg.descricao
                if rpg.mestre:
                    entity.mestre = database.session.get(MestreEntity, rpg.mestre.id)
                entity.jogadores = [
                    database.session.get(UsuarioEntity, usuario.id) 
                    for usuario in rpg.jogadores
                ]
                if len(entity.jogadores) != 0:
                    for jogador in entity.jogadores:
                        if jogador.id not in [j.id for j in rpg.jogadores]:
                            entity.jogadores.remove(jogador)
                entity.generos = [
                    database.session.get(GeneroEntity, genero.id) 
                    for genero in rpg.generos
                ]
                if len(entity.generos) != 0:
                    for genero in entity.generos:
                        if genero.id not in [g.id for g in rpg.generos]:
                            entity.generos.remove(genero)
                database.session.commit()
                return RPG.from_entity(entity)
            except Exception as exception:
                database.session.rollback()
                raise exception
