from .models import Persona
from rest_framework import viewsets, permissions

class PersonasViewSet(viewsets.ModelViewSet):
  queryset = Persona.object.all()
  permission_classes = [permissions.AllowaAny]
  serializer_class = PersonaSerializer