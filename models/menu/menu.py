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
        return 1

    def handle_input(self, user_input, handler):
        if user_input == 1:
            user = self.createUser(handler)
            # Update the current user in the handler
            if user: 
                handler.currentUser = user  
                return UserMenu()
            else:
                return CreateUser()  

    def createUser(self, handler):
        response = {}
        for key, value in self.options.items():
            response[key] = input(f"{value}")
        user = handler.userList.addUser(response)
        if user:
            print(f"Usuario creado correctamente. Bienvenido {user.name}")
        else:
            raise ValueError("No se pudo crear el usuario. El nombre ya existe. Vuelva a intentarlo.")
        return user

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
        self.printTitle()
        self.printDescription()
        return 1
        
    def handle_input(self, user_input, handler):
        if user_input == 1:
            newEvent = {}
            for key, value in self.options.items():
                newEvent[key] = input(f"{value}")
                # TODO: This response is just an example of what info the menu will gather. With this, the
                # future class "Event" can create a new Event.
            handler.currentUser.addEvent(newEvent)
            return UserMenu()
            
class ShowEvents(MenuDisplay):
    # TODO
    # This Menu let's the user create a new event.
    def __init__(self):
        super().__init__()
        self.title = "PROXIMOS EVENTOS"
        self.description = ""
        self.options = {
            "1" : "Todavía no estan implementados"
        }
    def launchMenu(self):
        self.printTitle()
        self.printDescription()
        return 1
    def handle_input(self, user_input, handler):
        for user in handler.userList.users:
            print(user)
            for event in user.events:
                print(f"{event['id']}. {event["title"]}")

