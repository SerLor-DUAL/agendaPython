from models import User

class UserList:
    users = []
    def addUser(self, user):
        self.users.append(user)
    def deleteUserByID(self, userID):
        self.users.pop(userID)
    def getUsers(self):
        return self.users