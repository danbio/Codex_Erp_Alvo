"""Administração de turmas."""

from __future__ import annotations

from django.contrib import admin

from apps.turmas.models import Turma


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    """Configuração da administração de turmas."""

    list_display = ("nome", "curso", "professor", "data_inicio", "ativa")
    list_filter = ("curso", "ativa")
    search_fields = ("nome", "curso__nome", "professor__nome")
