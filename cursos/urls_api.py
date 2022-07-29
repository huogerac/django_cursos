from django.urls import path

from cursos import views_api

urlpatterns = [
    path('cursos', views_api.listar_cursos, name='cursos.listar.aulas'),
]
