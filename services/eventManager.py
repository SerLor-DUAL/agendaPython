# services/eventManager.py
from models import Event

# Import necessary modules for type hinting and datetime handling
from typing import Optional
from datetime import datetime

class EventManager:
    def __init__(self, dbManager):
        self.db = dbManager

#---------------------#
#   CRUD for Event    #
#---------------------#

    # Function to create a new event for a user in the database
    def create(self, event:Event):
        
        #  Checks if parameters are provided and if they are valid
        if event is None:
            raise ValueError("Event object is required.")
        if not isinstance(event, Event):
            raise TypeError("Expected an instance of Event.")
        
        # Prepare the insert query
        insertQuery = """ INSERT INTO EVENTS_NEV (nev_title, nev_description, nev_startTime, nev_endTime)
                          VALUES (%s, %s, %s, %s) RETURNING nev_id """
        params = (event.title, event.description, event.startTime, event.endTime)
        
        # Execute the insert query with the event details
        result = self.db.executeQuery(insertQuery, params)
        
        if result:
            event.id = result[0][0]  # Get the generated event ID from the result
        return event # Return the event

#---------------------------------------------------------------------------------------------------------------------#

    # Function to read an event's details from the database
    def read(self, eventId: int):

        # Prepare the select query
        selectQuery = """ SELECT nev_id, nev_title, nev_description, nev_startTime, nev_endTime
                            FROM EVENTS_NEV 
                           WHERE nev_id = %s """
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
        
        # Prepare the update query and parameters
        updateQuery = """ UPDATE EVENTS_NEV
                             SET nev_title = %s, nev_description = %s, nev_startTime = %s, nev_endTime = %s
                           WHERE nev_id = %s """
        params = (event.title, event.description, event.startTime, event.endTime, event.id)
        
        # Execute the update query with the event details
        self.db.executeQuery(updateQuery, params)

#---------------------------------------------------------------------------------------------------------------------#

    # Function to delete an event from the database
    def delete(self, eventId: int):
        
        # Prepare the delete query and parameters
        deleteQuery = """ DELETE FROM EVENTS_NEV WHERE nev_id = %s """
        params = (eventId,)
        
        # Execute the query with the event ID
        self.db.executeQuery(deleteQuery, params)