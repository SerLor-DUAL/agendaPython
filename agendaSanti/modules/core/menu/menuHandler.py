from modules.core.menu.menu import MenuDisplay, CreateUser, UserMenu, CreateEventMenu, ShowEvents

class menuHandler:
    def __init__(self):
        self.isRunning = True
        self.active_menu = MenuDisplay()
    def showMenu(self):
        user_input = self.active_menu.launchMenu()
        if type(self.active_menu) is MenuDisplay:
            if user_input == 1:
                self.active_menu = CreateUser()

        elif isinstance(self.active_menu, CreateUser):
            self.active_menu = UserMenu()

        elif isinstance(self.active_menu, UserMenu):
            if user_input == 1:
                self.active_menu = CreateEventMenu()
            elif user_input == 2:
                self.active_menu = ShowEvents()

        elif isinstance(self.active_menu, ShowEvents):
            input("Presione ENTER para volver al menú de usuario.")
            self.active_menu = UserMenu()

        elif isinstance(self.active_menu, CreateEventMenu):
            input("Presione ENTER para volver al menú de usuario.")
            self.active_menu = UserMenu()