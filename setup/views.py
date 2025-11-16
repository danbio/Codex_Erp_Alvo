"""Views responsáveis pelas páginas institucionais do projeto."""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class PaginaInicialView(TemplateView):
    """Exibe o conteúdo público da aplicação, incentivando o login."""

    template_name = "home.html"


class DashboardView(LoginRequiredMixin, TemplateView):
    """Painel interno protegido por autenticação."""

    template_name = "dashboard.html"
    login_url = "login"
