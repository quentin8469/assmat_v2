from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
# Create your views here.


def calendar_view(request, year=datetime.now().year, month=datetime.now().month):
    """
    add calendar in home.html
    """
    now = datetime.now()

    current_month = now.month
    current_year = now.year
    calendrier = HTMLCalendar().formatmonth(year, month)

    return render(request, "calendar/calendar.html", {"calendrier": calendrier})

