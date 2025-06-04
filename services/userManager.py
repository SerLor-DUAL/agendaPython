# services/eventManager.py
from models.generic.user import User
from models.generic.userList import UserList

# Import necessary modules for type hinting and datetime handling
from typing import Optional
from datetime import datetime

class UserManager:
    def __init__(self, dbManager):
        self.db = dbManager

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
        
        # Prepare the insert query
        insertQuery = """ INSERT INTO "USERS_NUE" (nue_id, nue_nickname, nue_recordcreation, nue_recordmodification)
                          VALUES (%s, %s, %s, %s)"""
        params = (user.id, user.nickname, datetime.now(), datetime.now())
        
        # Execute the insert query with the user details
        result = self.db.executeQuery(insertQuery, params)
        
        return user # Return the user

#---------------------------------------------------------------------------------------------------------------------#

    # Function to read an user's details from the database
    def read(self, userId: int):

        # Prepare the select query
        selectQuery = """ SELECT nue_id, nue_nickname, nue_recordcreation, nue_recordmodification
                            FROM "USERS_NUE"
                           WHERE nue_id = %s """
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

        # Prepare the update query and parameters
        updateQuery = """ UPDATE "USERS_NUE"
                             SET nue_nickname = %s, nue_recordmodification = %s
                           WHERE nue_id = %s """
        params = (user.nickname, datetime.now(), user.id)
        
        # Execute the update query with the user details
        self.db.executeQuery(updateQuery, params)

#---------------------------------------------------------------------------------------------------------------------#

    # Function to delete an user from the database
    def delete(self, userId: int):
        
        # Prepare the delete query and parameters
        deleteQuery = """ DELETE FROM "USERS_NUE" WHERE nue_id = %s """
        params = (userId,)
        
        # Execute the query with the user ID
        self.db.executeQuery(deleteQuery, params)
        
        
        
#---------------------------------------------------------------------------------------------------------------------#

    # Function to list all users in the database
    def list(self):
        
        # Prepare the select query to get all users
        selectQuery = """ SELECT nue_id, nue_nickname
                            FROM "USERS_NUE" """
        
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
        selectQuery = """ SELECT MAX(nue_id) FROM "USERS_NUE" """
        result = self.db.executeQuery(selectQuery)
        
        # If the result is not empty and the first element is not None, return the last ID + 1
        if result and result[0][0] is not None:
            return result[0][0] + 1
        # If no users exist, return 1 as the next ID
        else:
            return 1