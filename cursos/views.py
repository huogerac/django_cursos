from django.shortcuts import render

from .models import Curso

def pagina_inicial(request):
    context = {
        "cursos": []
    }
    return render(request, "cursos/pagina_inicial.html", context)


def listar_cursos(request):
    return render(request, 'cursos/listar_cursos.html')


def listar_aulas(request, pk):
    curso = Curso.objects.get(id=pk)
    context = {
        "curso": curso,
        "aulas": curso.aulas.all()
    }
    return render(request, 'cursos/listar_aulas.html', context)