from datetime import datetime
from zoneinfo import ZoneInfo
from blogapp.settings import TIME_ZONE


def now():
    """
    returns the current ts for the configured time zone
    """
    tz = ZoneInfo(TIME_ZONE)
    return datetime.now(tz)

