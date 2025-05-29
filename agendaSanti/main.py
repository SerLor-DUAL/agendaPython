from modules.core.menu.menuHandler import MenuHandler

handler = MenuHandler()
while handler.isRunning:
    handler.showMenu()

