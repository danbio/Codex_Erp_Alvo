"""Mapeamento de URLs raiz do projeto Alvo Gestão."""

from __future__ import annotations

from django.contrib import admin
from django.urls import URLPattern, include, path

urlpatterns: list[URLPattern] = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("alunos/", include("apps.alunos.urls")),
    path("professores/", include("apps.professores.urls")),
    path("cursos/", include("apps.cursos.urls")),
    path("turmas/", include("apps.turmas.urls")),
    path("matriculas/", include("apps.matriculas.urls")),
    path("financeiro/", include("apps.financeiro.urls")),
    path("configuracoes/", include("apps.configuracoes.urls")),
    path("", include("apps.dashboard.urls")),
]
