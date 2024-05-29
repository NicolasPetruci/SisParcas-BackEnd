from src.domain.models import Usuario
from src.infra.db.entities import UsuarioEntity
from src.infra.db.config import DBConnectionHandler
from src.data.interfaces import UsuarioRepositoryInterface
from typing import List

class UsuarioRepository(UsuarioRepositoryInterface):

    @classmethod
    def insert(cls, usuario: Usuario) -> Usuario:
        with DBConnectionHandler() as database:
            try: 
                entity = UsuarioEntity(
                    nome = usuario.nome
                )
                database.session.add(entity)
                database.session.commit()
                return Usuario(entity.id, entity.nome)
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def find_all(cls)->List[Usuario]:
        with DBConnectionHandler() as database:
            try:
                usuarios = (
                    Usuario(entity.id, entity.nome) 
                    for entity in 
                    database.session
                        .query(UsuarioEntity)
                        .all()
                )
                return usuarios
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def delete_by_id(cls, id: int) -> Usuario:
        with DBConnectionHandler() as database:
            try:
                entity = database.session.get(UsuarioEntity, id)
                if entity is None:
                    return None
                database.session.delete(entity)
                database.session.commit()
                return Usuario(entity.id, entity.nome)
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def find_by_id(cls, id: int) -> Usuario:
        with DBConnectionHandler() as database:
            try:
                entity = (
                    database.session.get(UsuarioEntity, id)
                )
                if entity is None:
                    return None
                return Usuario(entity.id, entity.nome)
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def update(cls, usuario: Usuario) -> Usuario:
        with DBConnectionHandler() as database:
            try:
                entity = database.session.get(UsuarioEntity, usuario.id)
                if entity is None:
                    return None
                entity.nome = usuario.nome
                database.session.commit()
                return Usuario(entity.id, entity.nome)
            except Exception as exception:
                database.session.rollback()
                raise exception
