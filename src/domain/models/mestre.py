from .usuario import Usuario
from .rpg import RPG

class Mestre:
    def __init__(
        self,
        id = None,
        ativo = None,
        usuario = None,
        rpgs = None,
    ):
        self.__id = id
        self.__ativo = ativo
        self.__usuario = usuario
        self.__rpgs = rpgs   

    @property
    def id(self):
        return self.__id
    @property
    def ativo(self):
        return self.__ativo
    @property
    def usuario(self):
        return self.__usuario
    @property
    def rpgs(self):
        return self.__rpgs

    def set_id(self, id):
        self.__id = id
        return self
        
    def set_ativo(self, ativo):
        self.__ativo = ativo
        return self
        
    def set_usuario(self, usuario):
        self.__usuario = usuario
        return self
        
    def set_rpgs(self, rpgs):
        self.__rpgs = rpgs
        return self
        
    @staticmethod
    def from_entity(entity):
        return Mestre(
            id = entity.id,
            ativo = entity.ativo,
            usuario = Usuario.from_entity(entity.usuario),
            rpgs = [RPG.from_entity_sem_mestre(rpg) for rpg in entity.rpgs],
        )

    @staticmethod
    def from_entity_sem_rpg(entity):
        return Mestre(
            id = entity.id,
            ativo = entity.ativo,
            usuario = Usuario.from_entity(entity.usuario),
        )
    def to_json(self):
        return {
            "id": self.id,
            "ativo": self.ativo,
            "usuario": self.usuario.to_json(),
            "rpgs": [rpg.to_json_sem_mestre() for rpg in self.rpgs],
        }
    def to_json_sem_rpg(self):
        return {
            "id": self.id,
            "ativo": self.ativo,
            "usuario": self.usuario.to_json(),
        }