from datetime import datetime, timedelta
class Payload:

    def __init__(self, username, cargo, id) -> None:
        self.username = username
        self.cargo = cargo
        self.id = id
        self.exp = datetime.utcnow() + timedelta(3600)

    def to_json(self):
        return {
            "username": self.username, 
            "cargo": self.cargo.upper(), 
            "id": self.id,
            "exp": self.exp.timestamp()
            }