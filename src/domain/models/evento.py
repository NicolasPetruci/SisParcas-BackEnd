from datetime import datetime
from .tipo_evento import TipoEvento
from .usuario import Usuario
from typing import List

class Evento():

    def __init__(
        self,
        id: int = None,
        nome: str = None,
        descricao: str = None,
        local: str = None,
        online: bool = None,
        data_hora: datetime = None,
        tipo_evento: TipoEvento = None,
        participantes: List[Usuario] = [],
    ) -> None:
        self.__id = id
        self.__nome = nome
        self.__descricao = descricao
        self.__local = local
        self.__online = online
        self.__data_hora = data_hora
        self.__tipo_evento = tipo_evento
        self.__participantes = participantes
    
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
    def local(self):
        return self.__local

    @property
    def online(self):
        return self.__online

    @property
    def data_hora(self):
        return self.__data_hora

    @property
    def tipo_evento(self):
        return self.__tipo_evento
    
    @property
    def participantes(self):
        return self.__participantes

    def set_id(self, id: int):
        self.__id = id

    def set_nome(self, nome: str):
        self.__nome = nome
    
    def set_descricao(self, descricao):
        self.__descricao = descricao

    def set_local(self, local):
        self.__local = local

    def set_online(self, online):
        self.__online = online

    def set_data_hora(self, data_hora):
        self.__data_hora = data_hora

    def set_tipo_evento(self, tipo_evento):
        self.__tipo_evento = tipo_evento

    def set_participantes(self, participantes):
        self.__participantes = participantes
    
    def adicionar_participante(self, participante):
        self.__participantes.append(participante)

    def remover_participante(self, participante):
        self.__participantes.remove(participante)

    @staticmethod
    def from_entity(entity):
        return Evento(
            entity.id, 
            entity.nome, 
            entity.descricao, 
            entity.local, 
            entity.online, 
            entity.data_hora,
            TipoEvento.from_entity(entity.tipo_evento),
            Usuario.list_from_entities(entity.participantes),
        )

    def to_json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao, 
            "local": self.local,
            "data_hora": self.data_hora,
            "tipo_evento": self.tipo_evento.to_json() if self.tipo_evento else None,
            "participantes": [p.to_json() for p in self.participantes]
        }
