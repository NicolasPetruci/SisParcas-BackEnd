
class Mestre:
    def __init__(
        self,
        id,
        ativo,
        id_usuario,
        usuario,
        rpgs,
    ):
        self.__id = id
        self.__ativo = ativo
        self.__id_usuario = id_usuario
        self.__usuario = usuario
        self.__rpgs = rpgs   

    @property
    def id(id):
        return self.__id
    @property
    def ativo(ativo):
        return self.__ativo
    @property
    def id_usuario(id_usuario):
        return self.__id_usuario
    @property
    def usuario(usuario):
        return self.__usuario
    @property
    def rpgs(rpgs):
        return self.__rpgs

    def set_id(self, id):
        self.__id = id

    def set_ativo(self, ativo):
        self.__ativo = ativo

    def set_id_usuario(self, id_usuario):
        self.__id_usuario = id_usuario

    def set_usuario(self, usuario):
        self.__usuario = usuario

    def set_rpgs(self, rpgs):
        self.__rpgs = rpgs

    @staticmethod
    def from_entity(entity):
        self.__id = id
        self.__ativo = ativo
        self.__id_usuario = id_usuario
        self.__usuario = usuario
        self.__rpgs = rpgs

    def to_json(self):
        return {
            "id": self.id,
            "ativo": self.ativo,
            "id_usuario": self.id_usuario,
            "usuario": self.usuario,
            "rpgs": self.rpgs,
        }