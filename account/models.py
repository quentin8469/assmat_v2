from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    """
        model to create a user
    """
    profile_picture = models.ImageField(upload_to="userpicture/",
                                        blank=True, null=True)
    adresse_postale = models.CharField(max_length=150, blank=True, null=True)
    code_postal = models.CharField(max_length=5, blank=True, null=True)
    ville = models.CharField(max_length=150, blank=True, null=True)
    tel_fix = models.CharField(max_length=10, blank=True, null=True)
    tel_mob = models.CharField(max_length=10, blank=True, null=True)
    date_anniv = models.DateTimeField(blank=True, null=True)
    num_secu = models.CharField(max_length=13, blank=True, null=True)
    max_enfants = models.IntegerField(blank=True, null=True)
    num_agrement = models.CharField(max_length=6, blank=True, null=True)
    date_agrement = models.DateTimeField(blank=True, null=True)
    ass_civil = models.CharField(max_length=20, blank=True, null=True)
    ass_auto = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f'{self.username}- {self.first_name}- {self.last_name}'
