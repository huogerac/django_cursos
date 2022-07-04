from django.shortcuts import render

def pagina_inicial(request):
    context = {
        "cursos": []
    }
    return render(request, "cursos/pagina_inicial.html", context)


def listar_cursos(request):
    return render(request, 'cursos/listar_cursos.html')