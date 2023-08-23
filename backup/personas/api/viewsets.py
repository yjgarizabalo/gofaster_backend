from ..models import Persona
from rest_framework import generics, viewsets
from .serializer import PersonaSerializer

# Create your views here.
class PersonasView(generics.ListAPIView):
  queryset = Persona.objects.all()
  serilizer_class = PersonaSerializer
