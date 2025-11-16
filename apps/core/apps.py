"""Configuração do app Core."""

from django.apps import AppConfig


class CoreConfig(AppConfig):
    """App central para componentes compartilhados."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.core"
    verbose_name = "Core"
