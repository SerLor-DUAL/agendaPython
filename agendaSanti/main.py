from modules.core.menu import menu

launchingMenu = menu.MenuDisplay()
input = launchingMenu.launchMenu()

if input == 2:

    launchingMenu = menu.CreateEventMenu()
    launchingMenu.launchMenu()
