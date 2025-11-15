"""URLs do módulo de matrículas."""

from __future__ import annotations

from django.urls import URLPattern, path

from apps.matriculas import views

app_name = "matriculas"

urlpatterns: list[URLPattern] = [
    path("", views.MatriculaListView.as_view(), name="lista"),
    path("nova/", views.MatriculaCreateView.as_view(), name="criar"),
    path("<int:pk>/editar/", views.MatriculaUpdateView.as_view(), name="editar"),
    path("<int:pk>/excluir/", views.MatriculaDeleteView.as_view(), name="excluir"),
]
