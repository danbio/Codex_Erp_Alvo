from django.contrib import admin
from django.urls import include, path

from setup.views import home

urlpatterns = [
    # Url de administração
    path("admin/", admin.site.urls),
    # Autenticação de usuários
    path("accounts/", include("django.contrib.auth.urls")),
    # Página inicial
    path("", home, name="home"),
]
