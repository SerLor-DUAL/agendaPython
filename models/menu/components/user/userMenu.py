# menu/components/userMenu.py
#from importlib import import_module



from ...baseMenu import BaseMenu



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

    def handleInput(self, userInput: str, manager) -> "BaseMenu":
        """
        Handle user selection from user menu.
        
        Args:
            userInput: User's selection
            manager: MenuManager instance
            
        Returns:
            Next menu to display
        """
        
        if userInput == "1":
            from models.menu.components.event.createEventMenu import CreateEventMenu
            return CreateEventMenu()
            
        elif userInput == "2":
            # This is a good practice to avoid cicling imports.
            from models.menu.components.event.showEventsMenu import ShowEventsMenu
            return ShowEventsMenu()
            
        elif userInput == "3":
            manager.currentUser = None
            print("\nSesión cerrada exitosamente.")
            # Use dynamic import to avoid circular dependency
            #main_menu_module = import_module("models.menu.components.mainMenu")
            #return main_menu_module.MainMenu()
            from models.menu.components.user.userMenu import UserMenu
            return UserMenu()
            
        else:
            print("\nOpción inválida. Por favor intente nuevamente.")
            return self