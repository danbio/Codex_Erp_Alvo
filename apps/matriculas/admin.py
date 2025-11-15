"""Administração das matrículas."""

from __future__ import annotations

from django.contrib import admin

from apps.matriculas.models import Matricula


@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    """Configuração da administração das matrículas."""

    list_display = ("aluno", "turma", "data_matricula", "status")
    list_filter = ("status", "turma__curso")
    search_fields = ("aluno__nome", "turma__nome")
