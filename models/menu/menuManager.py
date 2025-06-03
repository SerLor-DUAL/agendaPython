# menu/menuManager.py
from typing import Optional
from ..generic.user import User
from ..generic.userList import UserList
from .baseMenu import BaseMenu
from .components.mainMenu import MainMenu
from ...db.dbManager import DbManager
from ...services.userManager import UserManager

class MenuManager:
    """
    Central controller for managing menu navigation and application state.
    """
    
    def __init__(self):
        self.isRunning: bool = True
        self.activeMenu: BaseMenu = MainMenu()
        self.currentUser: Optional[User] = None
        self.userList: UserList = UserList()
        self.dbManager: Optional[DbManager] = None
        self.userManager: Optional[UserManager] = None
        self.loadUsers()
        
    def loadUsers(self):
      
        # Database connection parameters
        # TODO : Move these to a configuration file or environment variables
        host = "localhost"
        port = 5433
        database = "i.SERGIO.2025.0"
        user = "sergio"
        password = "sergio"
        
        # Initialize DbManager y UserManager
        self.dbManager = DbManager(host, port, database, user, password)
        self.userManager = UserManager(self.dbManager)
        
        # Assign the database users to the userList
        self.userList = UserList(self.userManager.list())  # Load all users from the database

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