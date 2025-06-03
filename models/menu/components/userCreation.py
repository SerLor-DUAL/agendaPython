# menu/components/userCreation.py
from components import MenuDisplay, UserMenu

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