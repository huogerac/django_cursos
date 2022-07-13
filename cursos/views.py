from django.shortcuts import render

from .models import Curso


def pagina_inicial(request):
    return render(request, "cursos/pagina_inicial.html")


def listar_cursos(request):
    cursos = Curso.objects.all().order_by('nome')
    context = {
        'cursos': cursos,
    }
    return render(request, 'cursos/listar_cursos.html', context)


def listar_aulas(request, pk):
    curso = Curso.objects.get(id=pk)
    context = {
        "curso": curso,
        "aulas": curso.aulas.all()
    }
    return render(request, 'cursos/listar_aulas.html', context)
