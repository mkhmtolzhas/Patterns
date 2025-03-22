from UIFactory import UIFactory
from WindowsFactory import WindowsFactory

def create_ui(factory: UIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    print(button.click())
    print(checkbox.render())



if __name__ == "__main__":
    create_ui(WindowsFactory())