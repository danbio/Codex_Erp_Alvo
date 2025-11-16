"""Administração de professores."""

from __future__ import annotations

from django.contrib import admin

from apps.professores.models import Professor


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    """Configuração da listagem de professores no admin."""

    list_display = ("nome", "email", "telefone", "ativo")
    list_filter = ("ativo",)
    search_fields = ("nome", "email", "especialidade")
