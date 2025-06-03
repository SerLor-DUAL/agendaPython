# menu/menuManager.py
from typing import Optional
from models import User, UserList
from menu import BaseMenu, MainMenu

class MenuManager:
    """
    Central controller for managing menu navigation and application state.
    """
    
    def __init__(self):
        self.isRunning: bool = True
        self.activeMenu: BaseMenu = MainMenu()
        self.currentUser: Optional[User] = None
        self.userList: UserList = UserList()

    def run(self) -> None:
        """
        Main application loop.
        Handles menu navigation and error management.
        """
        while self.isRunning:
            try:
                # Display current menu and get user input
                userInput = self.activeMenu.launch()
                
                # Process input and get next menu
                nextMenu = self.activeMenu.handleInput(userInput, self)
                
                # Update active menu
                self.activeMenu = nextMenu
                
            except ValueError as e:
                print(f"\nError: {e}")
                input("Presione Enter para continuar...")
                self.activeMenu = MainMenu()
                
            except KeyboardInterrupt:
                print("\nSaliendo del programa...")
                self.isRunning = False
                
            except Exception as e:
                print(f"\nError inesperado: {e}")
                self.isRunning = False
                raise

    def exit(self) -> None:
        """Cleanly exit the application."""
        self.isRunning = False