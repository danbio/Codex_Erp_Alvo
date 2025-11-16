"""URLs do módulo de turmas."""

from __future__ import annotations

from django.urls import URLPattern, path

from apps.turmas import views

app_name = "turmas"

urlpatterns: list[URLPattern] = [
    path("", views.TurmaListView.as_view(), name="lista"),
    path("nova/", views.TurmaCreateView.as_view(), name="criar"),
    path("<int:pk>/editar/", views.TurmaUpdateView.as_view(), name="editar"),
    path("<int:pk>/excluir/", views.TurmaDeleteView.as_view(), name="excluir"),
]
