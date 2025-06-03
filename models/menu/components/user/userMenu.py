# menu/components/userMenu.py
from components import CreateEventMenu, ShowEventsMenu, MainMenu
from menu import MenuManager, BaseMenu

class UserMenu(BaseMenu):
    """
    Main menu for authenticated users.
    Provides access to user-specific functionality.
    """
    
    def __init__(self):
        super().__init__()
        self.title = "MENÚ DE USUARIO"
        self.description = "Seleccione una opción:"
        self.options = {
            "1": "Crear nuevo evento",
            "2": "Ver mis eventos",
            "3": "Cerrar sesión"
        }

    def handleInput(self, userInput: str, manager: MenuManager) -> BaseMenu:
        """
        Handle user selection from user menu.
        
        Args:
            userInput: User's selection
            manager: MenuManager instance
            
        Returns:
            Next menu to display
        """
        
        if userInput == "1":
            return CreateEventMenu()
            
        elif userInput == "2":
            return ShowEventsMenu()
            
        elif userInput == "3":
            manager.currentUser = None
            print("\nSesión cerrada exitosamente.")
            return MainMenu()
            
        else:
            print("\nOpción inválida. Por favor intente nuevamente.")
            return self