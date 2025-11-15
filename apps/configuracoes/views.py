"""Views do módulo de configurações."""

from __future__ import annotations

from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from apps.configuracoes.forms import ConfiguracaoEmpresaForm
from apps.configuracoes.models import ConfiguracaoEmpresa
from apps.core.views import ViewComTituloEBreadcrumb


class ConfiguracaoEmpresaUpdateView(LoginRequiredMixin, SuccessMessageMixin, ViewComTituloEBreadcrumb, UpdateView):
    """Atualiza a configuração da empresa."""

    model = ConfiguracaoEmpresa
    form_class = ConfiguracaoEmpresaForm
    template_name = "configuracoes/configuracao_empresa_formulario.html"
    success_url = reverse_lazy("configuracoes:empresa")
    success_message = "Configurações atualizadas com sucesso!"
    titulo_pagina = "Configurações da empresa"
    breadcrumb_rotulo = "Configurações"
    breadcrumb_url = None

    def get_object(self, queryset: Any | None = None) -> ConfiguracaoEmpresa:  # type: ignore[override]
        """Retorna a instância única de configuração."""

        return ConfiguracaoEmpresa.get_singular()

