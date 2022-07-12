from django.shortcuts import render

from .models import Curso


def pagina_inicial(request):
    context = {
        "cursos": []
    }
    return render(request, "cursos/pagina_inicial.html", context)


def listar_cursos(request):
    context = {
        "cursos": Curso.objects.all().order_by('nome')
    }
    return render(request, 'cursos/listar_cursos.html', context)
