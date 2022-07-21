from django.urls import path

from . import views

urlpatterns = [
    path("<pk>/aulas", views.listar_aulas, name='cursos.listar.aulas'),
    path('listar/', views.listar_cursos, name='cursos.listar.tudo'),
    path("novo/", views.NovoCursoView.as_view(), name="cursos.novo"),
    path("alterar/<pk>", views.AlterarCursoView.as_view(), name="cursos.alterar"),
    path("like/<pk>", views.like_no_curso, name="cursos.like_no_curso"),
    path("api/like/<pk>", views.api_like_no_curso, name="api.cursos.like_no_curso"),
    path('', views.pagina_inicial, name='cursos.inicio'),
    path('form', views.cursos_form, name='cursos.form'),
]