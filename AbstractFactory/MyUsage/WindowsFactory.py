from Checkbox import Checkbox
from UIFactory import UIFactory
from Button import Button

class WindowsFactory(UIFactory):
    def create_button(self) -> Button:
        return WindowsButton()
    
    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()



class WindowsButton(Button):
    def render(self) -> str:
        return "Rendered Windows button"
    
    def click(self) -> str:
        return "Clicked Windows button"
    

class WindowsCheckbox(Checkbox):
    def render(self) -> str:
        return "Rendered Windows button"
    
    def select(self) -> str:
        return "Selected Windows button"
