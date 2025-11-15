"""URLs do módulo financeiro."""

from __future__ import annotations

from django.urls import URLPattern, path

from apps.financeiro import views

app_name = "financeiro"

urlpatterns: list[URLPattern] = [
    path("", views.PagamentoListView.as_view(), name="lista"),
    path("novo/", views.PagamentoCreateView.as_view(), name="criar"),
    path("<int:pk>/editar/", views.PagamentoUpdateView.as_view(), name="editar"),
    path("<int:pk>/excluir/", views.PagamentoDeleteView.as_view(), name="excluir"),
]
