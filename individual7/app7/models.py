from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
import uuid


    
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.first_name}|{self.user.last_name}"


class Estado(models.Model):
    estado_choice = (
        ('P', 'Pendiente'),
        ('E', 'En proceso'),
        ('C', 'Completado'),
    )
    estado = models.CharField(max_length=1, choices=estado_choice)

    def __str__(self):
        return f"Objeto {self.pk} - Estado: {self.get_estado_display()}"

class Categoria(models.Model):
    CATEGORIA_CHOICES = (
        ('T', 'Trabajo'),
        ('H', 'Hogar'),
        ('C', 'Casa'),
    )
    nombre = models.CharField(max_length=1, choices=CATEGORIA_CHOICES)

    def __str__(self):
        return f"{self.get_nombre_display()}"


class Tareas(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_publicación = models.DateTimeField(blank=True, null=True)
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    categorias = models.ForeignKey(Categoria, on_delete=models.CASCADE)


    def publicar(self):
        self.fecha_publicación = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo