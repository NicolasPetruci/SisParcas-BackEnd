from typing import List
from .usuario import Usuario
from .genero import Genero
from importlib import import_module

class RPG:
    
    def __init__(
        self,
        id: int = None,
        nome: str = None,
        descricao: str = None,
        mestre: Usuario = None,
        jogadores: List[Usuario] = [],
        generos: List[Genero] = [],
    ):
        self.__id = id
        self.__nome = nome
        self.__descricao = descricao
        self.__mestre = mestre
        self.__jogadores = jogadores
        self.__generos = generos
    
    @property
    def id(self):
        return self.__id
    @property
    def nome(self):
        return self.__nome
    @property
    def descricao(self):
        return self.__descricao
    @property
    def mestre(self):
        return self.__mestre
    @property
    def jogadores(self):
        return self.__jogadores
    @property
    def generos(self):
        return self.__generos

    def set_id(self, id):
        self.__id = id
    
    def set_nome(self, nome):
        self.__nome = nome
    
    def set_descricao(self, descricao):
        self.__descricao = descricao
    
    def set_mestre(self, mestre):
        self.__mestre = mestre
    
    def set_jogadores(self, jogadores):
        self.__jogadores = jogadores
    
    def set_generos(self, generos):
        self.__generos = generos
    
    def adicionar_jogador(self, jogador):
        self.__jogadores.append(jogador)
    

    def remover_jogador(self, jogador):
        self.__jogadores.remove(jogador)


    @staticmethod
    def from_entity(entity):
        mestre_class = import_module('src.domain.models')
        return RPG(
            entity.id,
            entity.nome,
            entity.descricao,
            mestre_class.Mestre.from_entity_sem_rpg(entity.mestre),
            [Usuario.from_entity(jogador) for jogador in entity.jogadores],
            [Genero.from_entity(genero) for genero in entity.generos],
        )
    @staticmethod
    def from_entity_sem_mestre(entity):
        mestre_class = import_module('src.domain.models')
        return RPG(
            entity.id,
            entity.nome,
            entity.descricao,
            [Usuario.from_entity(jogador) for jogador in entity.jogadores],
            [Genero.from_entity(genero) for genero in entity.generos],
        )

    def to_json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao,
            "mestre": self.mestre.to_json_sem_rpg(),
            "jogadores": [o.to_json() for o in self.jogadores],
            "generos": [o.to_json() for o in self.generos],
        }
    
    def to_json_sem_mestre(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao,
            "jogadores": [o.to_json() for o in self.jogadores],
            "generos": [o.to_json() for o in self.generos],
        }
    