from django.contrib import admin

from .models import Autor, Curso, Aula, CursoLikes

admin.site.register(Autor)
admin.site.register(Curso)
admin.site.register(Aula)
admin.site.register(CursoLikes)
