"""Administração das configurações."""

from __future__ import annotations

from django.contrib import admin

from apps.configuracoes.models import ConfiguracaoEmpresa


@admin.register(ConfiguracaoEmpresa)
class ConfiguracaoEmpresaAdmin(admin.ModelAdmin):
    """Administração das configurações da empresa."""

    list_display = ("nome", "cnpj", "email")
    search_fields = ("nome", "cnpj")
