from django.urls import path

from enderecos import views

urlpatterns = [
    path("<cep>", views.detalhe, name="enderecos.detalhe"),
]
