from datetime import date

class Usuario():

    def __init__(
        self,
        nome: str,
        email: str,
        telefone: str,
        senha: str,
        aniversario: date,
        cargo: Cargo,
        id: int = None,
    ) -> None:
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone
        self.__senha = senha
        self.__aniversario = aniversario
        self.__id_cargo = id_cargo
    
    @property
    def id(self):
        return self.__id
        
    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self._email

    @property
    def telefone(self):
        return self._telefone

    @property
    def senha(self):
        return self._senha

    @property
    def aniversario(self):
        return self._aniversario

    @property
    def id_cargo(self):
        return self._id_cargo

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

    def set_id_cargo(self, id_cargo):
        self.__id_cargo = id_cargo

