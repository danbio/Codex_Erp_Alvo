from django.contrib import admin
from django.urls import include, path

from setup.views import DashboardView, PaginaInicialView

urlpatterns = [
    # Url de administração
    path("admin/", admin.site.urls),
    # Autenticação de usuários
    path("accounts/", include("django.contrib.auth.urls")),
    # Página inicial
    path("", PaginaInicialView.as_view(), name="home"),
    # Painel autenticado
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
]
