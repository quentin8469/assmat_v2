from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from eventscalendar.views import calendar_view

urlpatterns = [
    path('', calendar_view, name="calendar"),
    path('<int:year>/<int:month>/', calendar_view, name="calendar")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)