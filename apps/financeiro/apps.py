"""Configuração do aplicativo financeiro."""

from __future__ import annotations

from django.apps import AppConfig


class FinanceiroConfig(AppConfig):
    """Configurações do módulo financeiro."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.financeiro"
    verbose_name = "Financeiro"
