from django.shortcuts import reverse, render
from django.views.generic.edit import CreateView, UpdateView

from .models import Curso
from .forms import CursoModelForm


def pagina_inicial(request):
    return render(request, "cursos/pagina_inicial.html")


def listar_cursos(request):
    ordem = request.GET.get("ordenacao", "nome")
    cursos = Curso.objects.all().order_by(ordem)
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


class CursoMixin(object):
    model = Curso
    form_class = CursoModelForm
    context_object_name = "curso"

    def get_success_url(self):
        return reverse("cursos.listar.tudo")


class NovoCursoView(CursoMixin, CreateView):
    template_name = "cursos/curso_novo.html"


class AlterarCursoView(CursoMixin, UpdateView):
    template_name = "cursos/curso_alterar.html"
