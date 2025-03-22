from Checkbox import Checkbox
from UIFactory import UIFactory
from Button import Button

class LinuxFactory(UIFactory):
    def create_button(self) -> Button:
        return LinuxButton()
    
    def create_checkbox(self) -> Checkbox:
        return LinuxCheckbox()
        
        

class LinuxButton(Button):
    def render(self) -> str:
        return "Rendered Linux button"
    
    def click(self) -> str:
        return "Clicked Linux button"
    

class LinuxCheckbox(Checkbox):
    def render(self) -> str:
        return "Rendered Linux button"
    
    def select(self) -> str:
        return "Selected Linux button"
