# menu/menuManager.py

from components import MenuDisplay
from models import UserList

class MenuManager:
    def __init__(self):
        self.isRunning = True
        self.active_menu = MenuDisplay()
        self.currentUser = None
        self.userList = UserList() 

    def showMenu(self):
        user_input = self.active_menu.launchMenu()
        try:
            # We give to handle_input the user input and the handler itself
            self.active_menu = self.active_menu.handle_input(user_input, self)
        except Exception as e:
            # If an error occurs, reset to the main menu
            print(f"Ha ocurrido un error al procesar la entrada: {e}")
            self.active_menu = MenuDisplay()  
