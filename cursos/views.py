from django.shortcuts import render

def pagina_inicial(request):
    return render(request, "cursos/pagina_inicial.html")
