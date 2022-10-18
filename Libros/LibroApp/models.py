from django.db import models
from django.utils import timezone

"""modelo 1: SON LOS DATOS PARA LOS USUARIOS"""

class usuario(models.Model):
    nombre=models.CharField(max_length=60)
    apellido=models.CharField(max_length=60)
    edad=models.IntegerField()
    correo=models.EmailField()

""""modelo 2: DATOS PARA GUARDAR Y CLASIFICAR LIBROS"""

class libros(models.Model):
    nombreLibro=models.CharField(max_length=60)
    autor=models.CharField(max_length=60)
    capitulos=models.IntegerField()
    categoria=models.CharField(max_length=60)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_punlicacion=models.DateTimeField(null=True, blank=True) #PARA DECIRNOS SU FECHA DE PUBLICACIÓN

def publicacion(self):
    self.fecha_creacion = timezone.now() #GUARDA LOS DATOS DE PUBLICACIÓN
    self.save()

def __str__(self):
    return self.nombreLibro #RETORNA TITULO DEL LIBRO

"""modelo 3: DATOS DE USUARIOS ADMIN - ESTOS USUARIOS
SON LO QUE PODRÁN EDITAR, ELIMINAR Y MODIFICAR"""

class AdminUsuario(models.Model):
    nombreAdmin=models.CharField(max_length=60)
    correo1=models.EmailField()
    contrasenia=models.CharField(max_length=15)

