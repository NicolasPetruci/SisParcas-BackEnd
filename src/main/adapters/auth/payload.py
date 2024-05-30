class Payload:

    def __init__(self, username, cargo, id) -> None:
        self.username = username
        self.cargo = cargo
        self.id = id

    def to_json(self):
        return {
            "username": self.username, 
            "cargo": self.cargo.upper(), 
            "id": self._id
            }