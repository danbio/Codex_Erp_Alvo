"""Configuração do aplicativo de dashboard."""

from __future__ import annotations

from django.apps import AppConfig


class DashboardConfig(AppConfig):
    """Configurações do aplicativo de dashboard."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.dashboard"
    verbose_name = "Dashboard"
