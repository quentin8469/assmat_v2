from django.contrib import admin
from eventscalendar.models import Event
# Register your models here.


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', "start_time", "end_time")
