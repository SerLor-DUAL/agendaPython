from .user import User

class UserList:
    users = []
    def addUser(self, user):
        # No crear el usuario si el nombre ya existe
        name = user["name"]
        for existing_user in self.users:
            if existing_user.name == name:
                print(f"Ya existe un usuario con el nombre: {name}")
                return False

        newUserID = len(self.users) + 1
        newUser = User(newUserID, name)
        self.users.append(newUser)
        
    def deleteUserByID(self, userID):
        self.users.pop(userID)
    def getUsers(self):
        return self.users