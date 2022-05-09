from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from family.views import EnfantListView, EnfantDetailsView


app_name = 'family'

urlpatterns = [
    path('', EnfantListView.as_view(), name='dashboard'),
    path('<int:pk>/child_details/', EnfantDetailsView.as_view(), name='child_details')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
