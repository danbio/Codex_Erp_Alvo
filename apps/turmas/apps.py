"""Configuração do aplicativo de turmas."""

from __future__ import annotations

from django.apps import AppConfig


class TurmasConfig(AppConfig):
    """Configurações do aplicativo de turmas."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.turmas"
    verbose_name = "Turmas"
