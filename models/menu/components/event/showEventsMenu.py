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
        self.manager = None  # Será seteado desde el menú padre

    def launch(self) -> str:
        """Display all user events."""
        self.printTitle()
        self.printEvents()
        return self.getUserInput()
        
    def handleInput(self, userInput: str, manager) -> BaseMenu:
        self.manager = manager

        if userInput == "1":
            from ..user.userMenu import UserMenu
            return UserMenu()

        elif userInput == "2":
            from ..event.eventMenu import EventMenu
            # Aquí podrías pedir al usuario qué evento quiere editar
            # Para ejemplo, directamente retornamos EventMenu
            return EventMenu()

        else:
            print("\nOpción inválida. Por favor intente nuevamente.")
            return self

    def printEvents(self) -> None:
        """Print all events for the current user."""
        user = self.manager.currentUser
        user.events = self.manager.eventManager.listUserEvents(user)  # Fetch user's events

        if user and user.events:
            print("\nTus eventos actuales:")
            for idx, event in enumerate(user.events, 1):
                print(f"      {idx}. {event.title} - {event.startTime.strftime('%d/%m/%Y %H:%M')} a {event.endTime.strftime('%d/%m/%Y %H:%M')}")
            
            if len(user.events) > 0:
                print()  # Line break for better readability
        else:
            print("\nNo tienes eventos programados.\n")
