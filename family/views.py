from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from family.models import Employeur, Enfant, ContactUrgence
# Create your views here.
from eventscalendar.utils import calendar_view
from eventscalendar.models import Event
# listeView


class EnfantListView(ListView):
    model = Enfant
    context_object_name = "enfants"
    template_name = "family/home.html"

    def get_context_data(self, **kwargs):
        context = {}
        events_list = Event.objects.all()
        context['calendrier'] = calendar_view
        context['events'] = events_list
        return super().get_context_data(**context)


class EnfantDetailsView(DetailView):
    model = Enfant
    context_object_name = "enfant"
    template_name = "family/child_details.html"

    def get_context_data(self, **kwargs):
        context = {}
        contacts_urgences = ContactUrgence.objects.filter(enfant=self.kwargs['pk'])
        child_events = Event.objects.filter(child=self.kwargs['pk'])
        context['contacts_urgences'] = contacts_urgences
        context['calendrier'] = calendar_view
        context['events'] = child_events
        return super().get_context_data(**context)
