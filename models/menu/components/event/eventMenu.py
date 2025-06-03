from ...baseMenu import BaseMenu
from ..user.userMenu import UserMenu
from datetime import datetime
from dateutil import parser

class EventMenu(BaseMenu):
    """
    Menu for displaying user's events.
    """
    
    def __init__(self):
        super().__init__()
        self.title = "EDITAR EVENTO"
        self.options = {
                        "ID Evento": "Seleccione evento a editar",
                        "Enter": "Volver al menú principal"
                        }              
        self.fields = {
            "title": "Título del evento",
            "description": "Descripción (opcional)",
            "startDate": "Fecha de inicio (DD/MM/YYYY)",
            "startTime": "Hora de inicio (HH:MM)",
            "endDate": "Fecha de fin (DD/MM/YYYY)",
            "endTime": "Hora de fin (HH:MM)"
        } 

    def launch(self) -> str:
        """Display all user events."""
        self._print_title()
        return self.getUserInput()

    def collectEventData(self) -> dict:
        """Collect all required event data."""
        eventData = {}
        for field, prompt in self.fields.items():
            eventData[field] = input(f"{prompt}: ")
        return eventData
    


    def handleInput(self, userInput: str, manager) -> BaseMenu:
        if userInput == "":
            return UserMenu()
        else:
            event = manager.currentUser.getEventById()
            if event != None:
                newEventData = self.collectEventData()
                event = self.validateEventInformation(event, newEventData)
            else:
                print("No existe ese evento, vuelva a intentarlo.")
                self.handleInput(userInput, manager)
    @staticmethod
    def validateEventInformation(event, newEvent):
        if newEvent["title"] != "" and newEvent["title"] != event["title"]:
            event["title"] = newEvent["title"]
        if newEvent["description"] != "" and newEvent["description"] != event["description"]:
            event["description"] = newEvent["description"]

        # Validate and format dates
        if newEvent["startDate"] != "":
            NewEventStartDateTime = parser.parse(f'{newEvent["startDate"]} {newEvent["startTime"]}', dayfirst=True)
            if NewEventStartDateTime != event["startTime"]:
                event["starTime"] = NewEventStartDateTime
        if newEvent["endDate"] != "":
            NewEventEndDateTime = parser.parse(f'{newEvent["endDate"]} {newEvent["endTime"]}', dayfirst=True)
            if NewEventEndDateTime != event["endTime"]:
                event["endDate"] = NewEventEndDateTime
        return event