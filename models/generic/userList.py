from .user import User
class UserList:
    
    def __init__(self, users: list = None):
        if users is not None:
            self.users = users
        else:
            self.users = []

    def getUsers(self):
        return self.users
    
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