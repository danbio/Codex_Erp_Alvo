"""Configuração do aplicativo de cursos."""

from __future__ import annotations

from django.apps import AppConfig


class CursosConfig(AppConfig):
    """Configurações do aplicativo de cursos."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.cursos"
    verbose_name = "Cursos"
