# menu/components/userCreation.py
from ...baseMenu import BaseMenu
from .userMenu import UserMenu
from ....generic.user import User
class CreateUserMenu(BaseMenu):
    """
    Menu for creating new users.
    """
    
    def __init__(self):
        super().__init__()
        self.title = "CREAR NUEVO USUARIO"
        self.description = "Complete la siguiente información:"
        self.options = {
            "nickname": "Nombre de usuario"
        }

    def launch(self) -> dict:
        """Collect user information."""
        self.printTitle()
        return self.collectUserData()

    def collectUserData(self) -> dict:
        """Collect required user information."""
        userData = {}
        for field, prompt in self.options.items():
            userData[field] = input(f"{prompt}: ")
        return userData

    def handleInput(self, userData: dict, manager) -> "BaseMenu":
        """
        Process collected user data and create new user.
        """
        try:
            newNickname = userData.get("nickname", "").strip()
            
            if not newNickname:
                raise ValueError("El nombre de usuario no puede estar vacío.")
            
            # Check if the nickname already exists
            if manager.userList.userExists(newNickname):
                raise ValueError("El nombre de usuario ya existe. Por favor, elija otro.")
        
            # We assign a new ID to the user
            newUserId = manager.userManager.getNextId()
            
            # Create the new user
            #newId = manager.userManager.getNextId()
            newUser = manager.userManager.create(User(id = newUserId, nickname=newNickname))
            
            # Add the new user to the user list
            manager.userList.addUser(newUser)
            
            # Update the current user in the manager
            manager.currentUser = newUser
            
            print(f"\nUsuario creado exitosamente. Bienvenido, {newUser.nickname}!")
            return UserMenu()
            
        except ValueError as e:
            print(f"\nError: {e}")
            input("Presione Enter para intentar nuevamente...")
            return CreateUserMenu()
