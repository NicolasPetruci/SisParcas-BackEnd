from datetime import date
from .cargo import Cargo

class Usuario():

    def __init__(
        self,
        id: int,
        nome: str,
        email: str,
        telefone: str,
        senha: str,
        aniversario: date,
        cargo: Cargo,
    ) -> None:
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone
        self.__senha = senha
        self.__aniversario = aniversario
        self.__cargo = cargo
    
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
    def cargo(self):
        return self.__cargo

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

    def set_cargo(self, cargo):
        self.__cargo = cargo

    @staticmethod
    def from_entity(entity):
        return Usuario(
            entity.id, 
            entity.nome, 
            entity.email, 
            entity.telefone, 
            entity.senha, 
            entity.aniversario,
            Cargo.from_entity(entity=entity.cargo)
        )
    
    @staticmethod
    def list_from_entities(entities):
        return [from_entity(entity) for entity in entities]

    def to_json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email, 
            "telefone": self.telefone,
            "aniversario": self.aniversario,
            "cargo": self.cargo.to_json()
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
