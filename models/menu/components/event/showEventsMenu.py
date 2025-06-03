# menu/components/showEventsMenu.py
from importlib import import_module
from ...baseMenu import BaseMenu

class ShowEventsMenu(BaseMenu):
    """
    Menu for displaying user's events.
    """
    
    def __init__(self):
        super().__init__()
        self.title = "MIS EVENTOS"
        self.options = {
                        "1": "Volver al menú de usuario",
                        "2": "Editar Evento"
                        }               

    def launch(self) -> str:
        """Display all user events."""
<<<<<<< Updated upstream
        self._print_title()
        self.displayEvents()
        return self.getUserInput()
=======
        self.printTitle()
        return self.displayEvents()
>>>>>>> Stashed changes

    def displayEvents(self, manager: MenuManager) -> str:
        """Show user's events and get user input."""
<<<<<<< Updated upstream
=======
        print("\n1. Volver al menú de usuario\n")
        return input("Presione Enter para continuar...")

    def handleInput(self, userInput: str, manager) -> "BaseMenu":
        # Actual implementation would display the events here
>>>>>>> Stashed changes
        if manager.currentUser and manager.currentUser.events:
            print("\n" + "=" * 40)
            print("TUS EVENTOS".center(40))
            print("=" * 40)
            for idx, event in enumerate(manager.currentUser.events, start=1):
                print(f"\n{idx}. {event['title']}")
                print(f"   Inicio: {event['start'].strftime('%d/%m/%Y %H:%M')}")
                print(f"   Fin:    {event['end'].strftime('%d/%m/%Y %H:%M')}")
                if event['description']:
                    print(f"   Descripción: {event['description']}")
        else:
            print("\nNo tienes eventos programados.")
<<<<<<< Updated upstream

    def handleInput(self, userInput: str, manager: MenuManager) -> BaseMenu:
        if userInput == 1:
            return UserMenu()
        elif userInput == 2:
            return EventMenu()
=======
        
        input("\nPresione Enter para volver...")
        # Use dynamic import to avoid circular dependency
        
        userMenuModule = import_module("models.menu.components.user.userMenu")
        return userMenuModule.UserMenu()
>>>>>>> Stashed changes
