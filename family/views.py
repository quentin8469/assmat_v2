from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from family.models import Employeur, Enfant, ContactUrgence
# Create your views here.


# listeView


class EnfantListView(ListView):
    model = Enfant
    context_object_name = "enfants"
    template_name = "family/home.html"

