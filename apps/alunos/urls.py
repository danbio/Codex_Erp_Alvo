"""URLs relacionadas aos alunos."""

from __future__ import annotations

from django.urls import URLPattern, path

from apps.alunos import views

app_name = "alunos"

urlpatterns: list[URLPattern] = [
    path("", views.AlunoListView.as_view(), name="lista"),
    path("novo/", views.AlunoCreateView.as_view(), name="criar"),
    path("<int:pk>/editar/", views.AlunoUpdateView.as_view(), name="editar"),
    path("<int:pk>/excluir/", views.AlunoDeleteView.as_view(), name="excluir"),
]
