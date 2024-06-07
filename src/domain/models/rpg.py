from typing import List
from .usuario import Usuario
from .genero import Genero

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
        self.__jogadores.reemove(jogador)


    @staticmethod
    def from_entity(entity):
        return RPG(
            entity.id,
            entity.nome,
            entity.descricao,
            entity.mestre,
            entity.jogadores,
            entity.generos,
        )
    
    def to_json(self):
        return {
            "id": self.__id,
            "nome": self.__nome,
            "descricao": self.__descricao,
            "mestre": self.__mestre.to_json(),
            "jogadores": [o.to_json() for o in self.__jogadores],
            "generos": [o.to_json() for o in self.__generos],
        }
    