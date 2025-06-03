# menu/components/createEventMenu.py

from datetime import datetime
from dateutil import parser
from importlib import import_module

from ...baseMenu import BaseMenu

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
        self._print_header()
        return self.collectEventData()

    def collectEventData(self) -> dict:
        """Collect all required event data."""
        eventData = {}
        for field, prompt in self.fields.items():
            eventData[field] = input(f"{prompt}: ")
        return eventData

    def handleInput(self, eventData: dict, manager: "MenuManager") -> "BaseMenu":
        """
        Process collected event data and create new event.
        
        Args:
            event_data: Dictionary with event information
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
            
            # Create event dictionary
            event = {
                "title": eventData["title"],
                "description": eventData.get("description", ""),
                "start": startDatetime,
                "end": endDatetime,
                "created_at": datetime.now()
            }
            
            # Add event to current user
            manager.currentUser.addEvent(event)
            print("\nEvento creado exitosamente!")
            # Use dynamic import to avoid circular dependency
            user_menu_module = import_module("models.menu.components.user.userMenu")
            return user_menu_module.UserMenu()
            
        except ValueError as e:
            print(f"\nError: {e}")
            input("Presione Enter para corregir los datos...")
            return self