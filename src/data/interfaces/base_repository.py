from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')

class BaseRepository(ABC, Generic[T]):

    @abstractmethod
    def insert(self, obj: T)->T:pass