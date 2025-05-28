from modules.core.menu.menuHandler import menuHandler

handler = menuHandler()
while handler.isRunning:
    handler.showMenu()

