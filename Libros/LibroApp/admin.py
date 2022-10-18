from django.contrib import admin
from LibroApp.models import AdminUsuario, libros, usuario

# Register your models here.

admin.site.register(libros)
admin.site.register(usuario)
admin.site.register(AdminUsuario)