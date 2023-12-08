import calendar
import datetime

def getUnix():
    """Returns the Unix timestamp for 60 seconds from the time it was created."""
    future = datetime.datetime.utcnow() + datetime.timedelta(seconds=60)
    return calendar.timegm(future.timetuple())  