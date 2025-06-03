# menu/components/createEventMenu.py
from components import MenuDisplay, UserMenu

class CreateEventMenu(MenuDisplay):
    # This Menu let's the user create a new event.
    def __init__(self):
        super().__init__()
        self.title = "CREAR NUEVO EVENTO"
        self.description = "Completa los siguientes pasos:"
        self.options = {
            "title" : "Introducir título: ",
            "startDate" : "Seleccionar fecha de inicio (DD/MM/YYYY): ",
            "startTime" : "Seleccionar hora de inicio (HH:MM:SS): ",
            "endDate" : "Seleccionar fecha de fin (DD/MM/YYYY): ",
            "endTime" : "Seleccionar hora de fin (HH:MM:SS): ",
            "description" : "Agregar descripción: "
        }
    def launchMenu(self):
        self.printTitle()
        self.printDescription()
        return 1
        
    def handle_input(self, user_input, handler):
        if user_input == 1:
            newEvent = {}
            for key, value in self.options.items():
                newEvent[key] = input(f"{value}")
                # TODO: This response is just an example of what info the menu will gather. With this, the
                # future class "Event" can create a new Event.
            handler.currentUser.addEvent(newEvent)
            return UserMenu()