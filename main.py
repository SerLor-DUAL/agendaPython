from models import MenuManager

handler = MenuManager()
while handler.isRunning:
    handler.showMenu()

