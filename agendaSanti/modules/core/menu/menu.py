class MenuDisplay():
    def __init__(self):
        self.title = "Bienvenido a la agenda de registro"
        self.optionsText = "Elige una de las siguientes opciones."
        self.options = {
            1: "Ver proximos eventos",
            2: "Crear Evento"
        }
    def launchMenu(self):
        # I don't know if it should be done like this. But there are some different aproaches:
        # First -> Declare variables at the top of the funcion
        # Second -> Declare variables right before using them
        print(f"{self.title} \n {self.optionsText}")
        for key, value in self.options.items():
            print(f"{key}. {value}")
        return int(input())
    

class CreateEventMenu(MenuDisplay):
    def __init__(self):
        super().__init__()
        self.title = "Crear nuevo evento"
        self.optionsText = "Completa los siguientes pasos:"
        self.options = {
            "title" : "Introducir título: ",
            "date" : "Seleccionar fecha: ",
            "time": "Agregar hora: ",
            "description" : "Agregar descripción: "
        }
    def launchMenu(self):
        # I don't know if it should be done like this. But there are some different aproaches:
        # First -> Declare variables at the top of the funcion
        # Second -> Declare variables right before using them
        response = {}
        print(f"{self.title} \n {self.optionsText}")
        for key, value in self.options.items():
            response[key] = input(f"{value}")
        print(response)


