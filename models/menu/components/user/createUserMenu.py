# menu/components/userCreation.py
from ...baseMenu import BaseMenu
from .userMenu import UserMenu
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
        
        Args:
            userData: Dictionary with user information
            manager: MenuManager instance
            
        Returns:
            UserMenu on success, CreateUserMenu on failure
        """
        try:
            newUser = manager.userList.addUser(
                nickname=userData["nickname"],
            )
            
            manager.currentUser = newUser
            print(f"\nUsuario creado exitosamente. Bienvenido, {newUser.nickname}!")
            return UserMenu()
            
        except ValueError as e:
            print(f"\nError: {e}")
            input("Presione Enter para intentar nuevamente...")
            return CreateUserMenu()