"""Configuração do aplicativo de professores."""

from __future__ import annotations

from django.apps import AppConfig


class ProfessoresConfig(AppConfig):
    """Configurações do aplicativo de professores."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.professores"
    verbose_name = "Professores"
