from typing import Dict
class TipoEvento():

    def __init__(self, id: int, descricao: str):
        self.__id = id
        self.__descricao = descricao
    
    @property
    def id(self):
        return self.__id
        
    @property
    def descricao(self):
        return self.__descricao

    def set_id(self, id: int):
        self.__id = id


    def set_descricao(self, descricao: str):
        self.__descricao = descricao

    def to_json(self):
        return {
            "id": self.id,
            "descricao": self.descricao,
        }
    
    @staticmethod
    def from_entity(entity):
        return TipoEvento(
            entity.id,
            entity.descricao,
        )
