import datetime

# models/event.py
class Event:
    def __init__(self, id, title, description, startDate, startTime, endDate, endTime):
        self.id = id
        self.title = title
        self.description = description
        self.startTime = self.formatDate(startDate, startTime)
        self.endTime = self.formatDate(endDate, endTime)

    # Function to return a JSON representation of the Event object
    def __repr__(self):
        """Return a JSON representation of the Event object."""
        eventJSON = {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "start_time": self.startTime,
            "end_time": self.endTime,
            "eventUser": self.eventUser
        }
        return eventJSON
    
    @staticmethod
        # Function to manage the date and time format
        # Static method to format date and time into a datetime object
    def formatDate(date, hour):
        """Gathers information and returns a datetime"""
        day, month, year = map(int, date.split("/"))
        hour_, minute = map(int, hour.split(":"))
        return datetime.datetime(year, month, day, hour_, minute)

    # Function to edit an event's details in the database
    def editEvent(self, dbHandler, title = None, description = None, start_time = None, end_time = None):
        """Edit the event's details in the database."""
        
        #  Checks if parameters are provided and if they are valid
        if dbHandler is None:
            raise ValueError("Database handler is required to edit the event.")
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        
        # Prepare the update query and parameters
        updateQuery = """ UPDATE EVENTS_NEV
                             SET nev_title = %s, nev_description = %s, nev_startTime = %s, nev_endTime = %s
                           WHERE nev_id = %s """
        
        # Prepare the parameters
        params = (self.title, self.description, self.start_time, self.end_time, self.id)
        
        # Execute the query
        dbHandler.executeQuery(updateQuery, params)

    # Function to create a new event for a user in the database
    def createEvent(self, dbHandler):
        """Create a new event in the database."""
        
        # Check if the database handler is provided
        if dbHandler is None:
            raise ValueError("Database handler is required to create an event.")
        
        # Prepare the insert query
        insertQuery = """ INSERT INTO EVENTS_NEV (nev_title, nev_description, nev_startTime, nev_endTime)
                          VALUES (%s, %s, %s, %s) RETURNING nev_id """
        
        params = (self.title, self.description, self.startTime, self.endTime)
        
        # Execute the query and get the new event ID
        newEventId = dbHandler.executeQuery(insertQuery, params)
        self.id = newEventId[0][0]
        
    # Function to delete an event from the database
    def deleteEvent(self, dbHandler):
        """Delete the event from the database."""
        
        # Check if the database handler is provided
        if dbHandler is None:
            raise ValueError("Database handler is required to delete an event.")
        
        # Prepare the delete query
        deleteQuery = """ DELETE FROM EVENTS_NEV WHERE nev_id = %s """
        
        # Prepare the parameters
        params = (self.id)
        
        # Execute the query with the event ID
        dbHandler.executeQuery(deleteQuery, params)