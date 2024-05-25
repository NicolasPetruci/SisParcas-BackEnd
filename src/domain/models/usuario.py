
class Usuario():

    def __init__(self, id: int, nome: str) -> None:
        self.__id = id
        self.__nome = nome
    
    @property
    def id(self):
        return self.__id
        
    @property
    def nome(self):
        return self.__nome

    def set_id(self, id: int):
        self.__id = id


    def set_nome(self, nome: str):
        self.__nome = nome
