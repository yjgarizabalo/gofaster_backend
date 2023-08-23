from django.db import models

# Create your models here.
class Persona(models.Model):
  # Campos basicos
  identificacion = models.CharField(max_length=20, unique=True)
  primer_nombre = models.CharField(max_length=200)
  segundo_nombre = models.CharField(max_length=200, blank=True, null=True)
  primer_apellido = models.CharField(max_length=200)
  segundo_apellido = models.CharField(max_length=200, blank=True, null=True)
  correo = models.EmailField(max_length=100, unique=True)
  correo_personal = models.EmailField(max_length=100, null=True, blank=True)
  usuario = models.CharField(max_length=100, unique=True)
  celular = models.BigIntegerField(null=True)
  fecha_registro = models.DateTimeField(auto_now_add=True)
  fecha_elimino = models.DateTimeField(blank=True, null=True)
  estado = models.CharField(choices=[("1", "Activo"), ("0", "Inactivo")], default="1", max_length=10)

  def __str__(self):
    return self.primer_nombre