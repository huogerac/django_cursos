from django.urls import path

from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='cursos.inicio'),
    path('listar/meus-todos/', views.listar_cursos, name='cursos.listar.tudo'),
]