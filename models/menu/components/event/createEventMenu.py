# menu/components/createEventMenu.py
from dateutil import parser
from ...baseMenu import BaseMenu
from ..user.userMenu import UserMenu
from models.generic.event import Event

class CreateEventMenu(BaseMenu):
    """
    Menu for creating new calendar events.
    """
    
    def __init__(self):
        super().__init__()
        self.title = "CREAR NUEVO EVENTO"
        self.description = "Complete los detalles del evento:"
        self.fields = {
            "title": "Título del evento",
            "description": "Descripción (opcional)",
            "startDate": "Fecha de inicio (DD/MM/YYYY)",
            "startTime": "Hora de inicio (HH:MM)",
            "endDate": "Fecha de fin (DD/MM/YYYY)",
            "endTime": "Hora de fin (HH:MM)"
        }

    def launch(self) -> dict:
        """Collect event information from user."""
        self.printTitle()
        return self.collectEventData()

    def collectEventData(self) -> dict:
        """Collect all required event data."""
        eventData = {}
        for field, prompt in self.fields.items():
            eventData[field] = input(f"{prompt}: ")
        return eventData

    def handleInput(self, eventData: dict, manager) -> "BaseMenu":
        """
        Process collected event data and create new event.
        
        Args:
            eventData: Dictionary with event information
            manager: MenuManager instance
            
        Returns:
            UserMenu on success, self on failure
        """
        try:
            # Validate and format dates
            startDatetime = parser.parse(f'{eventData["startDate"]} {eventData["startTime"]}', dayfirst=True)
            endDatetime = parser.parse(f'{eventData["endDate"]} {eventData["endTime"]}', dayfirst=True)
            
            # Validate time range
            if endDatetime <= startDatetime:
                raise ValueError("La fecha/hora de fin debe ser posterior a la de inicio")
            
            # Assign the next event ID
            newEventId = manager.eventManager.getNextId()
            
            # Create event object
            event = Event(
                            id=newEventId,
                            title=eventData["title"],
                            description=eventData.get("description", ""),
                            startTime=startDatetime,
                            endTime=endDatetime
                        )

            # Create event into the database and adds this event to current user
            manager.eventManager.create(event, manager.currentUser)
            
            # Add the new event to the user event list
            manager.currentUser.events.append(event)
            
            # Notify user of success
            print("\nEvento creado exitosamente!")
            return UserMenu()
            
        except ValueError as e:
            print(f"\nError: {e}")
            input("Presione Enter para corregir los datos...")
            return self