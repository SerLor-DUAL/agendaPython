# menu/components/menuDisplay.py
from components import CreateUser

class MenuDisplay():
    def __init__(self):
        self.title = "AGENDA VIRTUAL PERSONAL"
        self.description = "Elige una de las siguientes opciones."
        self.options = {
            1: "Cree un usuario",
            2: "Ver usuarios",
        }
        
    def printTitle(self):
        print("=" * 40)
        print(f"        {self.title}        ")
        print("=" * 40)
        
    def printDescription(self):
        print(self.description)

    def launchMenu(self):
        # I don't know if it should be done like this. But there are some different approaches:
        # First -> Declare variables at the top of the function
        # Second -> Declare variables right before using them
        self.printTitle()
        self.printDescription()
        for key, value in self.options.items():
            print(f"{key}. {value}")
        return int(input())
    
    def showUsers(self, userList):
        print("=" * 40)
        print(f"        LISTA DE USUARIOS        ")
        print("=" * 40)
        if userList:
            for index, user in enumerate(userList):
                print(f"{index}. ID: {user.id}, Nombre: {user.name}")
        else:
            print("Aún no hay usuarios registrados.")
            
    def handle_input(self, user_input, handler):
        if user_input == 1:
            return CreateUser()
        elif user_input == 2:
            self.showUsers(handler.userList.getUsers())
            return MenuDisplay()
