from django.contrib import admin
from family.models import Employeur, Enfant, ContactUrgence
# Register your models here.


@admin.register(Enfant)
class EnfantAdmin(admin.ModelAdmin):
    list_display = ('nom', "prenom", "age")


@admin.register(Employeur)
class EmployeurAdmin(admin.ModelAdmin):
    list_display = ('nom', "prenom", "ass_mat")


@admin.register(ContactUrgence)
class ContactUrgenceAdmin(admin.ModelAdmin):
    list_display = ('nom', "prenom", "filiation", "employeur")