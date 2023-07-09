from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
import uuid

class Estado(models.Model):
    estado_choice = (
        ('Pendiente', 'Pendiente'),
        ('En proceso', 'En proceso'),
        ('Completado', 'Completado'),
    )
    estado = models.CharField(max_length=20, choices=estado_choice)

    def __str__(self):
        return f"Estado: {self.get_estado_display()}"

class Categoria(models.Model):
    CATEGORIA_CHOICES = (
        ('Casa', 'Casa'),
        ('Trabajo', 'Trabajo'),
        ('Estudio', 'Estudio'),
    )
    nombre = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)

    def __str__(self):
        return f"{self.get_nombre_display()}"

class Prioridad(models.Model):
    PRIORIDAD_CHOICES = (
        ('Alta', 'Alta'),
        ('Media', 'Media'),
        ('Baja', 'Baja'),
    )
    prioridad = models.CharField(max_length=10, choices=PRIORIDAD_CHOICES, null=True)

    def __str__(self):
        return f"{self.prioridad}"


class Tareas(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField(max_length=200)
    asignado_a = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tareas_asignadas', null=True)
    prioridad = models.ForeignKey(Prioridad, on_delete=models.CASCADE, null=True)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(blank=True, null=True)
    fecha_vencimiento = models.DateTimeField(blank=True, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tareas_creadas')
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    categorias = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    observaciones = models.TextField(blank=True, null=True)
    


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
    tareas = models.ManyToManyField(Tareas)

    def __str__(self):
        return f"{self.user.first_name}|{self.user.last_name}"
    
