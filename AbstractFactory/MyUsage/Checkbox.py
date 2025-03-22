from abc import ABC, abstractmethod

class Checkbox(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

    @abstractmethod
    def select(self) -> str:
        pass