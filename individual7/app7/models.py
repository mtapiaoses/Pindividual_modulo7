from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
import uuid

# Create your models here.
class Tareas(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_publicación = models.DateTimeField(blank=True, null=True)
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def publicar(self):
        self.fecha_publicación = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
    
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.first_name}|{self.user.last_name}"

