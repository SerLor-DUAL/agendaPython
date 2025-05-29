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
        # I don't know if it should be done like this. But there are some different aproaches:
        # First -> Declare variables at the top of the funcion
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
        if len(userList) > 0:
            for user in userList:
                print(f"{userList.index(user)}. {user}")
        else:
            print("Aún no hay usuarios registrados.")

    
class CreateUser(MenuDisplay):
    # This Menu let's the user create a new event.
    def __init__(self):
        super().__init__()
        self.title = "INICIAR USUARIO"
        self.description = ""
        self.options = {
            "name" : "Introduzca su usuario ",
        }
    def launchMenu(self):
        self.printTitle()

    def createUser(self):
        response = {}
        for key, value in self.options.items():
            response[key] = input(f"{value}")
        # TODO: This response is just an example of what info the menu will gather. With this, the
        # future class "Event" can create a new Event.
        return response

class UserMenu(MenuDisplay):
    # This Menu let's the user create a new event.
    def __init__(self):
        super().__init__()
        self.title = "MENU DE USUARIO"
        self.description = ""
        self.options = {
            "1" : "Cree un evento ",
            "2" : "Ver eventos creados "
        }
    def launchMenu(self):
        return super().launchMenu()

class CreateEventMenu(MenuDisplay):
    # This Menu let's the user create a new event.
    def __init__(self):
        super().__init__()
        self.title = "CREAR NUEVO EVENTO"
        self.description = "Completa los siguientes pasos:"
        self.options = {
            "title" : "Introducir título: ",
            "startDate" : "Seleccionar fecha de inicio (DD/MM/YYYY): ",
            "startTime" : "Seleccionar hora de inicio (HH:MM:SS): ",
            "endDate" : "Seleccionar fecha de fin (DD/MM/YYYY): ",
            "endTime" : "Seleccionar hora de fin (HH:MM:SS): ",
            "description" : "Agregar descripción: "
        }
    def launchMenu(self):
        response = {}
        self.printTitle()
        self.printDescription()
        for key, value in self.options.items():
            response[key] = input(f"{value}")
        # TODO: This response is just an example of what info the menu will gather. With this, the
        # future class "Event" can create a new Event.
        print(response)

class ShowEvents(MenuDisplay):
    # This Menu let's the user create a new event.
    def __init__(self):
        super().__init__()
        self.title = "PROXIMOS EVENTOS"
        self.description = ""
        self.options = {
            "1" : "Todavía no estan implementados"
        }
    def launchMenu(self):
        return super().launchMenu()
