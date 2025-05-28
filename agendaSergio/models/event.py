
# models/event.py
class Event:
    def __init__(event, id, title, description, startTime, endTime, user):
        event.id = id
        event.title = title
        event.description = description
        event.startTime = startTime
        event.endTime = endTime
        event.eventUser = user
    
    
    def __repr__(event):
        """Return a JSON representation of the Event object."""
        eventJSON = {
            "id": event.id,
            "title": event.title,
            "description": event.description,
            "start_time": event.startTime,
            "end_time": event.endTime,
            "eventUser": event.eventUser
        }
        return eventJSON
    
    
