from django.db import models
from family.models import CustomUser, Enfant
# Create your models here.


class Event(models.Model):
    """
    Model for the events calendar
    """
    title = models.CharField("Event Title", max_length=200)
    description = models.TextField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    assmat = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    child = models.ForeignKey(to=Enfant, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return f"{self.title} - {self.child}"

