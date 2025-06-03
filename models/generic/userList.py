from .user import User
class UserList:
    
    def __init__(self, users: list = None):
        if users is not None:
            self.users = users
        else:
            self.users = []

    def getUsers(self):
        return self.users
    
    # def addUser(self, user):
    #     # Don't create a user if the name already exists
    #     name = user["name"]
    #     for existingUser in self.users:
    #         if existingUser.name == name:
    #             print(f"Ya existe un usuario con el nombre: {name}")
    #             return None
    #     # Get new user ID
    #     newUserID = len(self.users) + 1
    #     newUser = User(newUserID, name)
    #     self.users.append(newUser)
    #     return newUser
    
    def deleteUserByID(self, userID):
        self.users.pop(userID)
    
    def userExists(self, nickname: str) -> bool:
        """
        Check if a user with the given nickname exists in the list.
        
        Args:
            nickname (str): The nickname to check.
        
        Returns:
            bool: True if user exists, False otherwise.
        """
        return any(user.nickname == nickname for user in self.users)
    
    def __str__(self):
        return "\n".join(f"ID: {user.id}, Nickname: {user.nickname}" for user in self.users)