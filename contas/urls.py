from django.contrib.auth import views as auth_views
from django.urls import path

from . import forms
from . import views

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
