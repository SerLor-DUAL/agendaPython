from .menu import MenuDisplay, CreateUser, UserMenu, CreateEventMenu, ShowEvents
from ..generic.userList import UserList

userList = UserList()
class MenuHandler:
    def __init__(self):
        self.isRunning = True
        self.active_menu = MenuDisplay()
        self.currentUser = None
    def showMenu(self):
        userInput = self.active_menu.launchMenu()
        if type(self.active_menu) is MenuDisplay:
            if userInput == 1:
                self.active_menu = CreateUser()
            if userInput == 2:
                self.active_menu.showUsers(userList.users)

        elif isinstance(self.active_menu, CreateUser):
            user = self.active_menu.createUser()
            result = userList.addUser(user)
            if result:
                print(f"Usuario creado correctamente. Bienvenido {user.name}")
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