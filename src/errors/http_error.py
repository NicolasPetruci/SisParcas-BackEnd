from typing import Dict

class HttpError(Exception):
    """Class to define errors in http"""

    def __init__(self, error: Dict):
        super().__init__(error["body"]["message"])
        self.message = error["body"]["message"]
        self.status_code = error["status_code"]
        self.name = error["body"]["name"]


    @staticmethod
    def error_400(message="Bad Request"):
        """HTTP 400"""

        return {"status_code": 400, "body": {"name": "Bad Request", "message": message}}

    @staticmethod
    def error_401(message="Unauthorized"):
        """HTTP 401"""

        return {"status_code": 401, "body": {"name": "Unauthorized", "message": message}}

    @staticmethod
    def error_403(message="Forbidden"):
        """HTTP 403"""

        return {"status_code": 403, "body": {"name": "Forbidden", "message": message}}
    @staticmethod
    def error_404(message="Not Found"):
        """HTTP 404"""

        return {"status_code": 404, "body": {"name": "Not Found", "message": message}}

    @staticmethod
    def error_409(message="Conflict"):
        """HTTP 409"""

        return {"status_code": 409, "body": {"name": "Conflict", "message": message}}

    @staticmethod
    def error_422(message="Unprocessable Entity"):
        """HTTP 422"""

        return {"status_code": 422, "body": {"name": "Unprocessable Entity", "message": message}}

    @staticmethod
    def error_500(message="Internal Server Error"):
        """HTTP 500"""

        return {"status_code": 500, "body": {"name": "Internal Server Error", "message": message}}