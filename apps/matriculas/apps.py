"""Configuração do aplicativo de matrículas."""

from __future__ import annotations

from django.apps import AppConfig


class MatriculasConfig(AppConfig):
    """Configurações do aplicativo de matrículas."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.matriculas"
    verbose_name = "Matrículas"
