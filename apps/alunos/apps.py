"""Configuração do aplicativo de alunos."""

from __future__ import annotations

from django.apps import AppConfig


class AlunosConfig(AppConfig):
    """Configurações do aplicativo de alunos."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.alunos"
    verbose_name = "Alunos"
