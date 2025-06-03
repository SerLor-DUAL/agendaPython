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
        self._print_title()
        self.displayEvents()
        return self.getUserInput()

    def displayEvents(self, manager: MenuManager) -> str:
        """Show user's events and get user input."""
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

    def handleInput(self, userInput: str, manager: MenuManager) -> BaseMenu:
        if userInput == 1:
            return UserMenu()
        elif userInput == 2:
            return EventMenu()
