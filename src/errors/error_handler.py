from .http_error import HttpError
from src.presentation.http_types import HttpResponse

def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, HttpError):

        return HttpResponse(
            status_code=error.status_code,
            body={
                "error": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )
    return HttpResponse(
    status_code=500,
    body={
        "error": [{
            "name": "Internal Server Error",
            "message": str(error)
        }]
    })