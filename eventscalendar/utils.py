from calendar import HTMLCalendar
from datetime import datetime
from eventscalendar.models import Event
# Create your views here.


def calendar_view(year=datetime.now().year, month=datetime.now().month):
    """
    add calendar in template
    """
    calendrier = HTMLCalendar().formatmonth(year, month)

    return calendrier


class CustomCalendar(HTMLCalendar):
    pass

