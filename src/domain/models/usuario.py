from datetime import date
from .cargo import Cargo
from typing import List

class Usuario():

    def __init__(
        self,
        id: int = None,
        nome: str = None,
        email: str = None,
        telefone: str = None,
        senha: str = None,
        aniversario: date = None,
        cargos: List[Cargo] = None,
    ) -> None:
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone
        self.__senha = senha
        self.__aniversario = aniversario
        self.__cargos = cargos
    
    @property
    def id(self):
        return self.__id
        
    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email

    @property
    def telefone(self):
        return self.__telefone

    @property
    def senha(self):
        return self.__senha

    @property
    def aniversario(self):
        return self.__aniversario

    @property
    def cargos(self):
        return self.__cargos

    def set_id(self, id: int):
        self.__id = id

    def set_nome(self, nome: str):
        self.__nome = nome
    
    def set_email(self, email):
        self.__email = email

    def set_telefone(self, telefone):
        self.__telefone = telefone

    def set_senha(self, senha):
        self.__senha = senha

    def set_aniversario(self, aniversario):
        self.__aniversario = aniversario

    def set_cargos(self, cargos):
        self.__cargos = cargos

    @staticmethod
    def from_entity(entity):
        return Usuario(
            entity.id, 
            entity.nome, 
            entity.email, 
            entity.telefone, 
            entity.senha, 
            entity.aniversario,
            [Cargo.from_entity(entity=cargo) for cargo in entity.cargos]
        )
    
    @staticmethod
    def list_from_entities(entities):
        return [Usuario.from_entity(entity) for entity in entities]

    def to_json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email, 
            "telefone": self.telefone,
            "aniversario": self.aniversario,
            "cargos": [cargo.to_json() for cargo in self.cargos]
        }

class UsuarioLogin():

    def __init__(
        self,
        email: str,
        senha: str
    ) -> None:
        self.__email = email
        self.__senha = senha

    @property
    def email(self):
        return self.__email

    @property
    def senha(self):
        return self.__senha
    

    def set_email(self, email):
        self.__email = email

    def set_senha(self, senha):
        self.__senha = senha
