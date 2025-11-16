"""Administração de cursos."""

from __future__ import annotations

from django.contrib import admin

from apps.cursos.models import Curso


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    """Configuração da administração de cursos."""

    list_display = ("nome", "carga_horaria", "valor", "ativo")
    list_filter = ("ativo",)
    search_fields = ("nome",)
