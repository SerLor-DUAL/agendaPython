#menu/baseMenu.py
from abc import ABC, abstractmethod
from typing import Dict, Any
class BaseMenu(ABC):
    """Abstract base class for all menu implementations."""
    
    def __init__(self):
        self.title: str = "Base Menu"
        self.description: str = "This is the base menu."
        self.options: Dict[str, str] = {}

    def launch(self) -> Any:
        """Display the menu and get user input."""
        self.printTitle()
        self.printDescription()
        return self.getUserInput()

    def printTitle(self) -> None:
        """Print the menu title with formatting."""
        print(f"\n{self.title}\n{'=' * len(self.title)}")

    def printDescription(self) -> None:
        """Print the menu description."""
        print(self.description)

    def getUserInput(self) -> Any:
        """Display options and get user input."""
        for key, value in self.options.items():
            print(f"{key}: {value}")
        return input("Seleccione una opción: ")

    @abstractmethod
    def handleInput(self, userInput: Any, manager) -> "BaseMenu":
        """
        Handle user input and return next menu to display.

        Args:
            userInput: The input provided by the user
            manager: Reference to the menu manager for state management

        Returns:
            Next menu to display
        """
        pass
    
    def validateInput(self, inputValue: str, validOptions: list) -> bool:
        """Validate if user input is in the list of valid options."""
        return inputValue in validOptions