from models.menu.menuHandler import MenuHandler

handler = MenuHandler()
while handler.isRunning:
    handler.showMenu()

