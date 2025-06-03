from models import MenuHandler

handler = MenuHandler()
while handler.isRunning:
    handler.showMenu()

