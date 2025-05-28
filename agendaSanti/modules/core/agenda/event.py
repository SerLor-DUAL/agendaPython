import datetime

class Event():
    def __init__(self, user, title, date):
        self._user = user
        self._title = title
        self._date = self.formatDate()

    def formatDate(self, date, hour):
        newDate = date.split("/")
        newHour = hour.split(":")
        return datetime.datetime(newDate[0], newDate[1], newDate[2], newHour[0], newHour[1])
