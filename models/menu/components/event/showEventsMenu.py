# menu/components/showEventsMenu.py
#from importlib import import_module
from ...baseMenu import BaseMenu
from ..user.userMenu import UserMenu

class ShowEventsMenu(BaseMenu):
    """
    Menu for displaying user's events.
    """
    
    def __init__(self):
        super().__init__()
        self.title = "MIS EVENTOS"
        self.options = {
                        "1": "Volver al menú de usuario"
                        }               

    def launch(self) -> str:
        """Display all user events."""
        self.printHeader()
        return self.displayEvents()

    def displayEvents(self) -> str:
        """Show user's events and get user input."""
        print("\n1. Volver al menú de usuario\n")
        return input("Presione Enter para continuar...")

    def handleInput(self, userInput: str, manager) -> "BaseMenu":
        # Actual implementation would display the events here
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
        
        input("\nPresione Enter para volver...")
        # Use dynamic import to avoid circular dependency
        #user_menu_module = import_module("models.menu.components.user.userMenu")
        #return user_menu_module.UserMenu()
        return UserMenu()
