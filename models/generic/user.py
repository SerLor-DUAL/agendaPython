from .event import Event
# models/user.py
class User:
    def __init__(user, id, nickname):
        user.id = id
        user.nickname = nickname 
        # List to hold events associated with the user
        user.events = [] 
        
    def __repr__(user):
        """Return a JSON representation of the User object.""" 
        selfJSON = {
            "id": user.id,
            "nickname": user.nickname,
            "events": [event.__repr__() for event in user.events]  # Include events in the JSON representation
        }
        return selfJSON
    
    # Add methods to manage events for the user
    def addEvent(user, newEvent):
        """Add an event to the user's list of events."""
        print(newEvent)
        eventToAdd = Event(
                        len(user.events) + 1,
                        newEvent["title"], 
                        newEvent["description"], 
                        newEvent["startDate"],
                        newEvent["startTime"],
                        newEvent["endDate"],
                        newEvent["endTime"]) 
                        # I don't need the user parameter here, as the event is associated with the user through the user's events list
                        #eventUser = user
        user.events.append(eventToAdd)  # Append the new event to the user's events list
    
    # List all events associated with the user
    def listEvents(user):
        """List all events associated with the user."""
        return [event.__repr__() for event in user.events]
    
    # Remove an event from the user's list of events
    def removeEvent(user, eventId):
        """Remove an event from the user's list of events by ID."""
        user.events.pop(eventId)  # Remove the event with the specified ID from the user's events list
    
    # Edit an existing event's details   
    def editEvent(user, eventId, title=None, description=None, start_time=None, end_time=None):
        """Edit an existing event's details."""
        user.events[eventId].editEvent(title, description, start_time, end_time)
