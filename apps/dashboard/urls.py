"""URLs do dashboard."""

from __future__ import annotations

from django.urls import URLPattern, path

from apps.dashboard.views import DashboardView

app_name = "dashboard"

urlpatterns: list[URLPattern] = [
    path("", DashboardView.as_view(), name="visao_geral"),
]
