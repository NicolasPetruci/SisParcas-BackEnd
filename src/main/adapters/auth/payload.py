from datetime import datetime, timedelta
class Payload:

    def __init__(self, username, cargos, id) -> None:
        self.username = username
        self.cargos = cargos
        self.id = id
        self.exp = datetime.utcnow() + timedelta(3600)

    def to_json(self):
        return {
            "username": self.username, 
            "cargos": [cargo.descricao.upper() for cargo in self.cargos], 
            "id": self.id,
            "exp": self.exp.timestamp()
            }