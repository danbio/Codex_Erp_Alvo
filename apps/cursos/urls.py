"""URLs do módulo de cursos."""

from __future__ import annotations

from django.urls import URLPattern, path

from apps.cursos import views

app_name = "cursos"

urlpatterns: list[URLPattern] = [
    path("", views.CursoListView.as_view(), name="lista"),
    path("novo/", views.CursoCreateView.as_view(), name="criar"),
    path("<int:pk>/editar/", views.CursoUpdateView.as_view(), name="editar"),
    path("<int:pk>/excluir/", views.CursoDeleteView.as_view(), name="excluir"),
]
