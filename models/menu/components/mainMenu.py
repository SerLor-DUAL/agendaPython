# menu/components/menuDisplay.py
from ...generic.userList import UserList
from ..baseMenu import BaseMenu
from .user.createUserMenu import CreateUserMenu


class MainMenu(BaseMenu):
    """
    Main menu of the application.
    First menu displayed when the application starts.
    """
    
    def __init__(self):
        super().__init__()
        self.title = "AGENDA VIRTUAL PERSONAL"
        self.description = "Bienvenido a su agenda virtual. Seleccione una opción:"
        self.options = {
            "1": "Crear un usuario",
            "2": "Ver usuarios existentes",
            "3": "Salir"
        }

    def handleInput(self, userInput: str, manager: "MenuManager") -> "BaseMenu":
        """
        Handle user selection from main menu.
        
        Args:
            userInput: User's selection
            manager: MenuManager instance for state management
            
        Returns:
            Next menu to display
        """
        if userInput == "1":
            return CreateUserMenu()
            
        elif userInput == "2":
            self.displayUsers(manager.userList)
            return self
            
        elif userInput == "3":
            manager.exit()
            return self
            
        else:
            print("\nOpción inválida. Por favor intente nuevamente.")
            return self

    def displayUsers(self, userList: UserList) -> None:
        """Display all registered users."""
        users = userList.getUsers()
        
        print("\n" + "=" * 40)
        print("USUARIOS REGISTRADOS".center(40))
        print("=" * 40)
        
        if not users:
            print("\nNo hay usuarios registrados.\n")
            return
            
        for idx, user in enumerate(users, start=1):
            print(f"{idx}. {user.name} (ID: {user.id})")
        
        input("\nPresione Enter para volver al menú principal...")