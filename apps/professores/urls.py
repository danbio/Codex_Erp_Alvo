"""URLs do módulo de professores."""

from __future__ import annotations

from django.urls import URLPattern, path

from apps.professores import views

app_name = "professores"

urlpatterns: list[URLPattern] = [
    path("", views.ProfessorListView.as_view(), name="lista"),
    path("novo/", views.ProfessorCreateView.as_view(), name="criar"),
    path("<int:pk>/editar/", views.ProfessorUpdateView.as_view(), name="editar"),
    path("<int:pk>/excluir/", views.ProfessorDeleteView.as_view(), name="excluir"),
]
