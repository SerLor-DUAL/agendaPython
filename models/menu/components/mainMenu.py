# menu/components/menuDisplay.py
from ...generic.userList import UserList
from ..baseMenu import BaseMenu
from .user.createUserMenu import CreateUserMenu
from .user.userMenu import UserMenu

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
            "2": "Entrar como usuario existente",
            "3": "Ver usuarios existentes",
            "4": "Salir"
        }

    def handleInput(self, userInput: str, manager) -> "BaseMenu":
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
            return self.loginUser(manager)
        
        elif userInput == "3":
            self.displayUsers(manager.userList)
            return self
            
        elif userInput == "4":
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
            print(f"{idx}. {user.nickname} (ID: {user.id})")
        
        input("\nPresione Enter para volver al menú principal...")
        
    def loginUser(self, manager) -> int:
        """
        Prompt user for nickname and check if it exists.
        
        Args:
            manager: MenuManager instance for state management
            
        Returns:
            User ID if found, otherwise -1
        """
        nickname = input("\nIngrese su nickname: ").strip()
        
        if not nickname:
            print("El nombre no puede estar vacío.")
            return self
        
        if manager.userList.userExists(nickname):
            user = next((user for user in manager.userList.getUsers() if user.nickname == nickname), None)
            if user:
                manager.currentUser = user
                print(f"\nBienvenido, {user.nickname}!")
                return UserMenu()
        else:
            print("\nUsuario no encontrado. Por favor intente nuevamente.")
        
        return self