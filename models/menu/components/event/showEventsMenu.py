# menu/components/showEventsMenu.py
from ...baseMenu import BaseMenu
from ..user.userMenu import UserMenu
from .eventMenu import EventMenu

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
        self.printTitle()
        return self.getUserInput()
        
    def handleInput(self, userInput: str, manager) -> BaseMenu:
        user = manager.currentUser
        if user and user.events:
            print("\nTus eventos actuales:")
            for idx, event in enumerate(user.events, 1):
                print(f"{idx}. {event['title']} - {event['start'].strftime('%d/%m/%Y %H:%M')} a {event['end'].strftime('%d/%m/%Y %H:%M')}")
        else:
            print("\nNo tienes eventos programados.")

        if userInput == "1":
            from ..user.userMenu import UserMenu
            return UserMenu()

        elif userInput == "2":
            from ..event.eventMenu import EventMenu
            # Aquí podrías pedir al usuario qué evento editar antes de cambiar de menú,
            # o pasar esa info al EventMenu
            return EventMenu()

        else:
            print("\nOpción inválida. Por favor intente nuevamente.")
            return self

