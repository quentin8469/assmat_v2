from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from family.views import EnfantListView


urlpatterns = [
    path('', EnfantListView.as_view(), name='dashboard')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
