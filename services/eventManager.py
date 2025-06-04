# services/eventManager.py
from models.generic.event import Event
from models.generic.user import User
import os

# Import necessary modules for type hinting and datetime handling
from typing import Optional
from datetime import datetime

class EventManager:
    def __init__(self, dbManager):
        self.db = dbManager
        self.envData = {
            "table": os.getenv("DB_EVENTS_TABLE"),
            "id": os.getenv("DB_EVENTS_TABLE_ID"),
            "title": os.getenv("DB_EVENTS_TABLE_TITLE"),
            "description": os.getenv("DB_EVENTS_TABLE_DESCRIPTION"),
            "startTime": os.getenv("DB_EVENTS_TABLE_STARTTIME"),
            "endTime": os.getenv("DB_EVENTS_TABLE_ENDTIME"),
            "recordCreation": os.getenv("DB_EVENTS_TABLE_RECORDCREATION"),
            "recordModification": os.getenv("DB_EVENTS_TABLE_RECORDMODIFICATION"),
            "userId": os.getenv("DB_EVENTS_TABLE_USER_ID")
        }

#---------------------#
#   CRUD for Event    #
#---------------------#

    # Function to create a new event for a user in the database
    def create(self, event:Event, user:User):
        
        #  Checks if parameters are provided and if they are valid
        if event is None:
            raise ValueError("Event object is required.")
        if not isinstance(event, Event):
            raise TypeError("Expected an instance of Event.")
        
        # Prepare the environment configuration for the query
        env = self.envData
        # Prepare the insert query with the events table configuration
        insertQuery = f"""
                            INSERT INTO "{env['table']}" ({env['id']}, {env['title']}, {env['description']}, {env['startTime']}, 
                                        {env['endTime']}, {env['recordCreation']}, {env['recordModification']}, {env['userId']})
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                            RETURNING {env['id']}
                        """
        params = (event.id, event.title, event.description, event.startTime, event.endTime, datetime.now(), datetime.now(), user.id)
        
        # Execute the insert query with the event details
        self.db.executeQuery(insertQuery, params)

        return event # Return the event

#---------------------------------------------------------------------------------------------------------------------#

    # Function to read an event's details from the database
    def read(self, eventId: int):

        # Prepare the environment configuration for the query
        env = self.envData
        # Prepare the select query
        selectQuery = f"""
                            SELECT  {env['id']},
                                    {env['title']},
                                    {env['description']},
                                    {env['startTime']},
                                    {env['endTime']}
                            FROM "{env['table']}"
                            WHERE  {env['id']} = %s
                        """
        params = (eventId,)
        
        # Execute the select query with the event ID
        result = self.db.executeQuery(selectQuery, params)
        
        # If no result is found, raise an error
        if not result:
            raise ValueError("Event not found.")

        # Extract the event details from the result
        row = result[0]

        return Event(
                    id=row[0],
                    title=row[1],
                    description=row[2],
                    startTime=row[3],
                    endTime=row[4]
                    )

#---------------------------------------------------------------------------------------------------------------------#

    # Function to edit an event's details in the database
    def update(self, event:Event, title: Optional[str] = None, description : Optional[str] = None, startTime : Optional[datetime] = None, endTime : Optional[datetime] = None):
        
        #  Checks if parameters are provided and if they are valid
        if event is None:
            raise ValueError("Event object is required.")
        if not isinstance(event, Event):
            raise TypeError("Expected an instance of Event.")
        if title is not None:
            event.title = title
        if description is not None:
            event.description = description
        if  startTime is not None:
            event.startTime = startTime
        if  endTime is not None:
            event.endTime = endTime
        
        # Prepare the environment configuration for the query
        env = self.envData
        # Prepare the update query and parameters
        updateQuery = f"""
                            UPDATE "{env['table']}"
                            SET {env['title']} = %s, {env['description']} = %s, {env['startTime']} = %s, {env['endTime']} = %s
                            WHERE {env['id']} = %s
                        """
        params = (event.title, event.description, event.startTime, event.endTime, event.id)
        
        # Execute the update query with the event details
        self.db.executeQuery(updateQuery, params)

#---------------------------------------------------------------------------------------------------------------------#

    # Function to delete an event from the database
    def delete(self, eventId: int):
        
        # Prepare the environment configuration for the query
        env = self.envData
        # Prepare the delete query and parameters
        deleteQuery = f"""
                            DELETE FROM "{env['table']}"
                            WHERE {env['id']} = %s
                        """
        params = (eventId,)
        
        # Execute the query with the event ID
        self.db.executeQuery(deleteQuery, params)

#---------------------------------------------------------------------------------------------------------------------#

    # Function to get the next event ID from the database
    def getNextId(self) -> int:
        """
        Get the last event ID from the database.
        
        Returns:
            int: The last event ID.
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
        # If no events exist, return 1 as the next ID
        else:
            return 1
        
    # Function to check if a user exists in the database by title for the selected user
    def eventExistsForUser(self, title: str, user:User) -> bool:
        """
        Check if a event with the given title for an user already exists in the database.
        
        Args:
            title (str): The title to check.
            user (User): The user to check the event for.
        
        Returns:
            bool: True if event exists, False otherwise.
        """
        
        # Prepare the environment configuration for the query
        env = self.envData
        selectQuery = f""" 
                            SELECT COUNT(*) 
                            FROM "{env['table']}"
                            WHERE {env['title']} = %s AND {env['userId']} = %s
                        """
        params = (title, user.id)
        result = self.db.executeQuery(selectQuery, params)
        
        # If the count is greater than 0, the event exists
        return result[0][0] > 0 if result else False