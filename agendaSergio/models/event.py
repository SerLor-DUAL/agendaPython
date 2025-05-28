
# models/event.py
class Event:
    def __init__(event, id, title, description, start_time, end_time, user):
        event.id = id
        event.title = title
        event.description = description
        event.start_time = start_time
        event.end_time = end_time
        event.eventUser = user
    
    
    def __repr__(event):
        """Return a JSON representation of the Event object."""
        eventJSON = {
            "id": event.id,
            "title": event.title,
            "description": event.description,
            "start_time": event.start_time,
            "end_time": event.end_time,
            "eventUser": event.user
        }
        return eventJSON
    
    
