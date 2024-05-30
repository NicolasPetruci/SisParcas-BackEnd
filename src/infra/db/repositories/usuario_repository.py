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
                    nome = usuario.nome,
                    email = usuario.email,
                    telefone = usuario.telefone,
                    senha = usuario.senha,
                    aniversario = usuario.aniversario,
                    cargo = usuario.cargo
                )
                database.session.add(entity)
                database.session.commit()
                return Usuario.from_entity(entity)
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def find_all(cls)->List[Usuario]:
        with DBConnectionHandler() as database:
            try:
                usuarios = (
                    Usuario.from_entity(entity)
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
                return Usuario.from_entity(entity)
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
                return Usuario.from_entity(entity)
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def update(cls, usuario: Usuario) -> Usuario:
        with DBConnectionHandler() as database:
            try:
                entity: UsuarioEntity = database.session.get(UsuarioEntity, usuario.id)
                if entity is None:
                    return None
                entity.nome = usuario.nome
                entity.aniversario = usuario.aniversario
                entity.email = usuario.email
                entity.telefone = usuario.telefone
                entity.cargo = usuario.cargo
                database.session.commit()
                return Usuario.from_entity(entity)
            except Exception as exception:
                database.session.rollback()
                raise exception
    
    @classmethod
    def find_user_by_email(cls, email: str) -> Usuario:
        with DBConnectionHandler() as database:
            try:
                entity = database.session.get(UsuarioEntity, email)
                if entity is None:
                    return None
                return Usuario.from_entity(entity)
            except Exception as exception:
                database.session.rollback()
                raise exception
