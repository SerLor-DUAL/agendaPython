#menu/baseMenu.py

class BaseMenu:
    """
    Base class for all menus.
    This class provides a structure for creating menus with a title, description, and options.
    """
    
    def __init__(self):
        self.title = "Base Menu"
        self.description = "This is the base menu."
        self.options = {}

    def launchMenu(self):
        """
        Displays the menu title, description, and options.
        Returns the user input.
        """
        self.printTitle()
        self.printDescription()
        return self.getUserInput()

    def printTitle(self):
        print(f"\n{self.title}\n{'=' * len(self.title)}")

    def printDescription(self):
        print(self.description)

    def getUserInput(self):
        for key, value in self.options.items():
            print(f"{key}: {value}")
        return input("Seleccione una opción: ")