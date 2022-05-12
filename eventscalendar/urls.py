from django.urls import path
from eventscalendar.views import calendar_view

urlpatterns = [
    path('', calendar_view, name="calendar")
]