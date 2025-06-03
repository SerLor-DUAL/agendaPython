# menu/components/userMenu.py
from components import MenuDisplay, CreateEventMenu, ShowEvents

class UserMenu(MenuDisplay):
    # This Menu let's the user create a new event.
    def __init__(self):
        super().__init__()
        self.title = "MENU DE USUARIO"
        self.description = ""
        self.options = {
            "1" : "Cree un evento ",
            "2" : "Ver eventos creados ",
            "3" : "Volver al menú principal"
        }
    def launchMenu(self):
        return super().launchMenu()
    def handle_input(self, user_input, handler):
        if user_input == 1:
            return CreateEventMenu()
        elif user_input == 2:
            return ShowEvents()
        elif user_input == 3:
            return MenuDisplay()