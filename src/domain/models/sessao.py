from typing import List
from src.domain.models import Usuario, RPG
from datetime import datetime

class Sessao:

    def __init__(
        self,
        id: int,
        nome: str,
        descricao: str,
        data_hora: datetime,
        temporada: int,
        numero: int,
        rpg: RPG,
        jogadores: List[Usuario],
    ):
        self.__id = id
        self.__nome = nome
        self.__descricao = descricao
        self.__data_hora = data_hora
        self.__temporada = temporada
        self.__numero = numero
        self.__rpg = rpg
        self.__jogadores = jogadores
    
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
    def data_hora(self):
        return self.__data_hora
    @property
    def temporada(self):
        return self.__temporada
    @property
    def numero(self):
        return self.__numero
    @property
    def rpg(self):
        return self.__rpg
    @property
    def jogadores(self):
        return self.__jogadores
    
    def set_id(self, id):
        self.__id = id
    def set_nome(self, nome):
        self.__nome = nome
    def set_descricao(self, descricao):
        self.__descricao = descricao
    def set_data_hora(self, data_hora):
        self.__data_hora = data_hora
    def set_temporada(self, temporada):
        self.__temporada = temporada
    def set_numero(self, numero):
        self.__numero = numero
    def set_rpg(self, rpg):
        self.__rpg = rpg
    def set_jogadores(self, jogadores):
        self.__jogadores = jogadores
    
    @staticmethod
    def from_entity(entity):
        return Sessao(
            id,
            nome,
            descricao,
            data_hora,
            temporada,
            numero,
            rpg,
            jogadores,            
        )

    def to_json(self):
        return {
            "id": self.__id,
            "nome": self.__nome,
            "descricao": self.__descricao,
            "data_hora": self.__data_hora,
            "temporada": self.__temporada,
            "numero": self.__numero,
            "rpg": self.__rpg,
            "jogadores": self.__jogadores,
        }
            