"""Configuração do aplicativo de configurações."""

from __future__ import annotations

from django.apps import AppConfig


class ConfiguracoesConfig(AppConfig):
    """Configurações gerais do aplicativo de configurações."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.configuracoes"
    verbose_name = "Configurações"
