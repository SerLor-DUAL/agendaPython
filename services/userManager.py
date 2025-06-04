# services/eventManager.py
from models.generic.user import User
from models.generic.userList import UserList
import os

# Import necessary modules for type hinting and datetime handling
from typing import Optional
from datetime import datetime

class UserManager:
    def __init__(self, dbManager):
        self.db = dbManager
        self.envData= {
            "table": os.getenv("DB_USERS_TABLE"),
            "id": os.getenv("DB_USERS_TABLE_ID"),
            "nickname": os.getenv("DB_USERS_TABLE_NICKNAME"),
            "recordCreation": os.getenv("DB_USERS_TABLE_RECORDCREATION"),
            "recordModification": os.getenv("DB_USERS_TABLE_RECORDMODIFICATION")
        }

#---------------------#
#   CRUD for User     #
#---------------------#

    # Function to create a new event for a user in the database
    def create(self, user:User):
        
        #  Checks if parameters are provided and if they are valid
        if user is None:
            raise ValueError("User object is required.")
        if not isinstance(user, User):
            raise TypeError("Expected an instance of User.")
        
        # Prepare the environment configuration for the query
        env = self.envData
        # Prepare the insert query
        insertQuery = f"""
                            INSERT INTO "{env['table']}" ({env['id']}, {env['nickname']}, {env['recordCreation']}, {env['recordModification']})
                            VALUES (%s, %s, %s, %s)
                        """
        params = (user.id, user.nickname, datetime.now(), datetime.now())
        
        # Execute the insert query with the user details
        self.db.executeQuery(insertQuery, params)
        
        return user # Return the user

#---------------------------------------------------------------------------------------------------------------------#

    # Function to read an user's details from the database
    def read(self, userId: int):

        # Prepare the environment configuration for the query
        env = self.envData
        # Prepare the select query
        selectQuery = f"""
                            SELECT {env['id']}, {env['nickname']}, {env['recordCreation']}, {env['recordModification']}
                            FROM "{env['table']}"
                            WHERE {env['id']} = %s
                        """
        params = (userId,)
        
        # Execute the select query with the user ID
        result = self.db.executeQuery(selectQuery, params)
        
        # If no result is found, raise an error
        if not result:
            raise ValueError("User not found.")

        # Extract the user details from the result
        row = result[0]

        return User(
                    id=row[0],
                    nickname=row[1]
                    )

#---------------------------------------------------------------------------------------------------------------------#

    # Function to edit an event's details in the database
    def update(self, user:User, nickname: Optional[str] = None):
        
        #  Checks if parameters are provided and if they are valid
        if user is None:
            raise ValueError("User object is required.")
        if not isinstance(user, User):
            raise TypeError("Expected an instance of User.")
        if nickname is not None:
            user.nickname = nickname

        # Prepare the environment configuration for the query
        env = self.envData
        # Prepare the update query and parameters
        updateQuery = f"""
                            UPDATE "{env['table']}"
                            SET {env['nickname']} = %s, {env['recordModification']} = %s
                            WHERE {env['id']} = %s
                        """
        params = (user.nickname, datetime.now(), user.id)
        
        # Execute the update query with the user details
        self.db.executeQuery(updateQuery, params)

#---------------------------------------------------------------------------------------------------------------------#

    # Function to delete an user from the database
    def delete(self, userId: int):
        
        # Prepare the environment configuration for the query
        env = self.envData
        # Prepare the delete query and parameters
        deleteQuery = f"""
                            DELETE FROM "{env['table']}"
                            WHERE {env['id']} = %s
                        """
        params = (userId,)
        
        # Execute the query with the user ID
        self.db.executeQuery(deleteQuery, params)
        
        
        
#---------------------------------------------------------------------------------------------------------------------#

    # Function to list all users in the database
    def list(self):
        
        # Prepare the environment configuration for the query
        env = self.envData
        # Prepare the select query to get all users
        selectQuery = f"""
                            SELECT {env['id']}, {env['nickname']}
                            FROM "{env['table']}"
                        """
        # Execute the select query
        result = self.db.executeQuery(selectQuery)
        
        # If no users are found, return an empty UserList
        if not result:
            return UserList() 
        
        # If users are found, return a UserList object
        users = [User(id=row[0], nickname=row[1]) for row in result]
        
        return UserList(users)  # Return the object UserList with the list of users from the database
    
#---------------------------------------------------------------------------------------------------------------------#

    # Function to get the next user ID from the database
    def getNextId(self) -> int:
        """
        Get the last user ID from the database.
        
        Returns:
            int: The last user ID.
        """
        
        # Prepare the environment configuration for the query
        env = self.envData
        selectQuery = f""" 
                            SELECT MAX({env['id']}) 
                            FROM "{env['table']}"
                        """
        result = self.db.executeQuery(selectQuery)
        
        # If the result is not empty and the first element is not None, return the last ID + 1
        if result and result[0][0] is not None:
            return result[0][0] + 1
        # If no users exist, return 1 as the next ID
        else:
            return 1
        
    # Function to check if a user exists in the database by nickname
    def userExists(self, nickname: str) -> bool:
        """
        Check if a user with the given nickname exists in the database.
        
        Args:
            nickname (str): The nickname to check.
        
        Returns:
            bool: True if user exists, False otherwise.
        """
        
        # Prepare the environment configuration for the query
        env = self.envData
        selectQuery = f""" 
                            SELECT COUNT(*) 
                            FROM "{env['table']}"
                            WHERE {env['nickname']} = %s
                        """
        params = (nickname,)
        result = self.db.executeQuery(selectQuery, params)
        
        # If the count is greater than 0, the user exists
        return result[0][0] > 0 if result else False