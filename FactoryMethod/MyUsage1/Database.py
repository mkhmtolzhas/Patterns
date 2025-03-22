from abc import ABC, abstractmethod
from Connection import Connection

class Database(ABC):
    @abstractmethod
    def factory_method(self) -> Connection:
        pass

    def connect(self) -> str:
        return self.factory_method().connect()