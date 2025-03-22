from abc import ABC, abstractmethod
from Checkbox import Checkbox
from Button import Button

class UIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass