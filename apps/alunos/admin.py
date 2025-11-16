"""Configuração do Django Admin para alunos."""

from __future__ import annotations

from django.contrib import admin

from apps.alunos.models import Aluno


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    """Administração de alunos."""

    list_display = ("nome", "email", "telefone")
    search_fields = ("nome", "email", "documento")
    list_filter = ("criado_em",)
