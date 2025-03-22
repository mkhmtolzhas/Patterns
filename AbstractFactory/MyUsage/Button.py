from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

    @abstractmethod
    def click(self) -> str:
        pass