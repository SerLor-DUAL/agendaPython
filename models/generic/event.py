# models/generic/event.py

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
                "startTime": self.startTime,
                "endTime": self.endTime,
                }
        
    # Function to return a JSON representation of the Event object
    def __repr__(self):
        """Return a JSON representation of the Event object."""
        eventJSON = {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "startTime": self.startTime,
            "endTime": self.endTime,
        }
        return eventJSON
    
    # Method to return the event details as a string  
    def __str__(self):
        """Returns a string representation of the event."""
        return f"Event(id={self.id}, title={self.title}, description={self.description}, startTime={self.startTime}, endTime={self.endTime})"  
    