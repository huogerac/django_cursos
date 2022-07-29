from django.http import JsonResponse

from cursos.models import Curso


def listar_cursos(request):
    cursos = Curso.objects.order_by('nome').select_related('autor').all()
    return JsonResponse(
        {
            'cursos': [curso.json_dict() for curso in cursos]
        })
