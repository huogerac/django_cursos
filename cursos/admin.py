from django.contrib import admin

from .models import Autor, Curso, Aula

admin.site.register(Autor)
admin.site.register(Curso)
admin.site.register(Aula)