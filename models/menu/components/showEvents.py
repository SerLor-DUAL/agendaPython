# menu/components/showEvents.py
from components import MenuDisplay

class ShowEvents(MenuDisplay):
    # TODO
    # This Menu let's the user create a new event.
    def __init__(self):
        super().__init__()
        self.title = "PROXIMOS EVENTOS"
        self.description = ""
        self.options = {
            "1" : "Todavía no estan implementados"
        }
    def launchMenu(self):
        self.printTitle()
        self.printDescription()
        return 1
    def handle_input(self, user_input, handler):
        for user in handler.userList.users:
            print(user)
            for event in user.events:
                print(f"{event['id']}. {event["title"]}")
