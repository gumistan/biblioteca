from django.contrib import admin

from .models import Autor, Categoria, Copia, Estudiante, Libro, Prestamo

admin.site.register(Categoria)
admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(Copia)
admin.site.register(Estudiante)
admin.site.register(Prestamo)
