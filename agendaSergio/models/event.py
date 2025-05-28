import datetime

# models/event.py
class Event:
    def __init__(event, id, title, description, startDate, startTime, endDate, endTime, user):
        event.id = id
        event.title = title
        event.description = description
        event.startTime = event.formatDate(startDate, startTime)
        event.endTime = event.formatDate(endDate, endTime)
        event.eventUser = user
    
    # Function to manage the date and time format
    def formatDate(date, hour):
        """Gathers information and returns a datetime"""
        newDate = date.split("/")
        newHour = hour.split(":")
        return datetime.datetime(newDate[0], newDate[1], newDate[2], newHour[0], newHour[1])

    # Function to edit an event's details
    def editEvent(event, title=None, description=None, start_time=None, end_time=None):
        """Edit event's details"""
        if title is not None:
            event.title = title
        if description is not None:
            event.description = description
        if start_time is not None:
            event.start_time = start_time
        if end_time is not None:
            event.end_time = end_time
        
    # Function to return a JSON representation of the Event object
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
    
    
