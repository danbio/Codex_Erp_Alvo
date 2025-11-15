"""URLs do módulo de configurações."""

from __future__ import annotations

from django.urls import URLPattern, path

from apps.configuracoes import views

app_name = "configuracoes"

urlpatterns: list[URLPattern] = [
    path("", views.ConfiguracaoEmpresaUpdateView.as_view(), name="empresa"),
]
