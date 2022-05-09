from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from family.models import Employeur, Enfant, ContactUrgence
# Create your views here.


# listeView


class EnfantListView(ListView):
    model = Enfant
    context_object_name = "enfants"
    template_name = "family/home.html"


class EnfantDetailsView(DetailView):
    model = Enfant
    context_object_name = "enfant"
    template_name = "family/child_details.html"

    def get_context_data(self, **kwargs):
        context = {}
        contacts_urgences = ContactUrgence.objects.filter(enfant=self.kwargs['pk'])
        context['contacts_urgences'] = contacts_urgences
        return super().get_context_data(**context)
