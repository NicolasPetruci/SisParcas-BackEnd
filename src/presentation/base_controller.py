from abc import ABC, abstractmethod
from src.presentation.http_types import HttpRequest, HttpResponse

class BaseController(ABC):

    @abstractmethod
    def handle(self, http_request: HttpRequest) -> HttpResponse: pass