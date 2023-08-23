from django.urls import path
from . import views
from .api.viewsets import PersonasView

# api version  gofaster

urlpatterns = [
  path('personas', PersonasView.as_view(), name=None),
]