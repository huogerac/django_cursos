from django.views.generic import TemplateView
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from . import forms

urlpatterns = [
    # LOGIN
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="contas/login.html",
            authentication_form=forms.LoginForm,
        ),
        name="contas.login",
    ),
    path("cadastrar/", views.UsuarioCreate.as_view(), name="contas.cadastrar"),
    path("logout/", auth_views.LogoutView.as_view(), name='contas.logout'),

]
