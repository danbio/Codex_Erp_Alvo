"""Views do módulo financeiro."""

from __future__ import annotations

from typing import Any

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import QuerySet
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from apps.core.views import ViewComTituloEBreadcrumb
from apps.financeiro.forms import PagamentoForm
from apps.financeiro.models import Pagamento


class PagamentoListView(LoginRequiredMixin, ViewComTituloEBreadcrumb, ListView):
    """Lista os pagamentos registrados."""

    model = Pagamento
    template_name = "financeiro/pagamento_lista.html"
    context_object_name = "pagamentos"
    titulo_pagina = "Pagamentos"
    breadcrumb_rotulo = "Pagamentos"
    breadcrumb_url = None

    def get_queryset(self) -> QuerySet[Pagamento]:  # type: ignore[override]
        """Ordena pagamentos pelo vencimento."""

        return Pagamento.objects.select_related("matricula", "matricula__aluno").order_by("data_vencimento")


class PagamentoCreateView(LoginRequiredMixin, SuccessMessageMixin, ViewComTituloEBreadcrumb, CreateView):
    """Registra um novo pagamento."""

    model = Pagamento
    template_name = "financeiro/pagamento_formulario.html"
    form_class = PagamentoForm
    success_url = reverse_lazy("financeiro:lista")
    success_message = "Pagamento criado com sucesso!"
    titulo_pagina = "Registrar pagamento"
    breadcrumb_rotulo = "Novo pagamento"
    breadcrumb_pai = (("Pagamentos", reverse_lazy("financeiro:lista")),)


class PagamentoUpdateView(LoginRequiredMixin, SuccessMessageMixin, ViewComTituloEBreadcrumb, UpdateView):
    """Atualiza um pagamento."""

    model = Pagamento
    template_name = "financeiro/pagamento_formulario.html"
    form_class = PagamentoForm
    success_url = reverse_lazy("financeiro:lista")
    success_message = "Pagamento atualizado com sucesso!"
    titulo_pagina = "Editar pagamento"
    breadcrumb_rotulo = "Editar pagamento"
    breadcrumb_pai = (("Pagamentos", reverse_lazy("financeiro:lista")),)


class PagamentoDeleteView(LoginRequiredMixin, ViewComTituloEBreadcrumb, DeleteView):
    """Remove um pagamento."""

    model = Pagamento
    template_name = "financeiro/pagamento_confirmar_exclusao.html"
    success_url = reverse_lazy("financeiro:lista")
    titulo_pagina = "Excluir pagamento"
    breadcrumb_rotulo = "Excluir pagamento"
    breadcrumb_pai = (("Pagamentos", reverse_lazy("financeiro:lista")),)

    def delete(self, request: Any, *args: Any, **kwargs: Any) -> Any:  # type: ignore[override]
        """Remove o pagamento com feedback."""

        messages.success(request, "Pagamento removido com sucesso!")
        return super().delete(request, *args, **kwargs)
