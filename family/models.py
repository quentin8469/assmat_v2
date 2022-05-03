from django.db import models

from account.models import CustomUser


# Create your models here.
class Employeur(models.Model):
    """
    Model for the creation of the Employeur model
    """
    email = models.EmailField(max_length=150, blank=True, null=True)
    photo = models.ImageField(upload_to="photo_employeur/", blank=True, null=True)
    nom = models.CharField(max_length=150, blank=True, null=True)
    prenom = models.CharField(max_length=150, blank=True, null=True)
    adresse_postale = models.CharField(max_length=150, blank=True, null=True)
    code_postal = models.CharField(max_length=5, blank=True, null=True)
    ville = models.CharField(max_length=150, blank=True, null=True)
    tel_fix = models.CharField(max_length=10, blank=True, null=True)
    tel_mob = models.CharField(max_length=10, blank=True, null=True)
    tel_doc = models.CharField(max_length=10, blank=True, null=True)
    date_anniv = models.DateTimeField(blank=True, null=True)
    num_urssaf = models.CharField(max_length=13, blank=True, null=True)
    ass_mat = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Employeur"
        verbose_name_plural = "Employeurs"

    def __str__(self):
        return f"{self.nom} - {self.prenom}"


class Enfant(models.Model):
    """
    Model for the creation of the Child model
    """
    photo = models.ImageField(upload_to="photo_enfant/", blank=True, null=True)
    nom = models.CharField(max_length=150, blank=True, null=True)
    prenom = models.CharField(max_length=150, blank=True, null=True)
    date_anniv = models.DateTimeField(blank=True, null=True)
    date_debut = models.DateTimeField(blank=True, null=True)
    date_fin = models.DateTimeField(blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    commentaire = models.TextField(blank=True, null=True)
    allergie = models.TextField(blank=True, null=True)
    parent = models.ForeignKey(to=Employeur, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Enfant"
        verbose_name_plural = "Enfants"

    def __str__(self):
        return f"{self.nom} - {self.prenom}- {self.age}"


class ContactUrgence(models.Model):
    """
    Model for the creation of the Contact urgence model
    """
    FILIATION_CHOICES = [
        ("Père", "Père"),
        ("Mère", "Mère"),
        ("Grand-mère", "Grand-mère"),
        ("Grand-père", "Grand-père"),
        ("Tante", "Tante"),
        ("Oncle", "Oncle"),
        ("Amis de la famille", "Amis de la famille"),
        ("Autres validé par la famille", "Autres validé par la famille"),
        ]

    nom = models.CharField(max_length=150, blank=True, null=True)
    prenom = models.CharField(max_length=150, blank=True, null=True)
    filiation = models.CharField(max_length=150,
                                 choices=FILIATION_CHOICES, blank=True, null=True)
    tel_fix = models.CharField(max_length=10, blank=True, null=True)
    tel_mob = models.CharField(max_length=10, blank=True, null=True)
    employeur = models.ForeignKey(to=Employeur, on_delete=models.CASCADE)
    enfant = models.ForeignKey(to=Enfant, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Contact Urgence"
        verbose_name_plural = "Contacts Urgences"

    def __str__(self):
        return f"{self.nom} - {self.prenom} - {self.filiation}"



