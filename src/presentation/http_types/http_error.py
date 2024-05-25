
class HttpError:
    """Class to define errors in http"""

    @staticmethod
    def error_400():
        """HTTP 400"""

        return {"status": 400, "body": {"error": "Bad Request"}}

    @staticmethod
    def error_401():
        """HTTP 401"""

        return {"status": 401, "body": {"error": "Unauthorized"}}

    @staticmethod
    def error_403():
        """HTTP 403"""

        return {"status": 403, "body": {"error": "Forbidden"}}

    @staticmethod
    def error_409():
        """HTTP 409"""

        return {"status": 409, "body": {"error": "Conflict"}}

    @staticmethod
    def error_422():
        """HTTP 422"""

        return {"status": 422, "body": {"error": "Unprocessable Entity"}}

    @staticmethod
    def error_500():
        """HTTP 500"""

        return {"status": 500, "body": {"error": "Internal Server Error"}}