from .user import User
class UserList:
    users = []
    def addUser(self, user):
        # Don't create a user if the name already exists
        name = user["name"]
        for existingUser in self.users:
            if existingUser.name == name:
                print(f"Ya existe un usuario con el nombre: {name}")
                return None
        # Get new user ID
        newUserID = len(self.users) + 1
        newUser = User(newUserID, name)
        self.users.append(newUser)
        return newUser
    
    def deleteUserByID(self, userID):
        self.users.pop(userID)
    def getUsers(self):
        return self.users