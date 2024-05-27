from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List

T = TypeVar('T')

class BaseRepository(ABC, Generic[T]):

    @abstractmethod
    def insert(self, obj: T)->T:pass

    @abstractmethod
    def find_all(self) -> List[T]: pass

    @abstractmethod
    def find_by_id(self, id: int) -> T: pass

    @abstractmethod
    def delete_by_id(self, id: int) -> T: pass

    @abstractmethod
    def update(self, obj: T) -> T: pass 
