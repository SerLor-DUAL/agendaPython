from .menu import MenuDisplay, CreateUser, UserMenu, CreateEventMenu, ShowEvents
from ..userList import UserList

userList = UserList()
class MenuHandler:
    def __init__(self):
        self.isRunning = True
        self.active_menu = MenuDisplay()
    def showMenu(self):
        userInput = self.active_menu.launchMenu()
        if type(self.active_menu) is MenuDisplay:
            if userInput == 1:
                self.active_menu = CreateUser()
            if userInput == 2:
                self.active_menu.showUsers(userList)

        elif isinstance(self.active_menu, CreateUser):
            self.active_menu = UserMenu()

        elif isinstance(self.active_menu, UserMenu):
            if userInput == 1:
                self.active_menu = CreateEventMenu()
            elif userInput == 2:
                self.active_menu = ShowEvents()

        elif isinstance(self.active_menu, ShowEvents):
            input("Presione ENTER para volver al menú de usuario.")
            self.active_menu = UserMenu()

        elif isinstance(self.active_menu, CreateEventMenu):
            input("Presione ENTER para volver al menú de usuario.")
            self.active_menu = UserMenu()