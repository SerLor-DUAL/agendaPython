# models/generic/event.py
import datetime
class Event:
    def __init__(self, id, title, description, startTime, endTime):
        self.id = id
        self.title = title
        self.description = description
        self.startTime = startTime
        self.endTime = endTime

    # Method to return the event details as a dictionary
    def to_dict(self):
        """Returns the event details as a dictionary it's useful for JSON."""
        return {
                "id": self.id,
                "title": self.title,
                "description": self.description,
                "start_time": self.startTime,
                "end_time": self.endTime,
                }
    # Function to return a JSON representation of the Event object
    def __repr__(self):
        """Return a JSON representation of the Event object."""
        eventJSON = {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "start_time": self.startTime,
            "end_time": self.endTime,
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
        
    # Method to return the event details as a string  
    def __str__(self):
        """Returns a string representation of the event."""
        return f"Event(id={self.id}, title={self.title}, description={self.description}, startTime={self.startTime}, endTime={self.endTime})"  
    