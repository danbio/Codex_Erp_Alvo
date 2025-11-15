"""Views do módulo de turmas."""

from __future__ import annotations

from typing import Any

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from apps.core.views import ViewComTituloEBreadcrumb
from apps.turmas.forms import TurmaForm
from apps.turmas.models import Turma


class TurmaListView(LoginRequiredMixin, ViewComTituloEBreadcrumb, ListView):
    """Lista as turmas cadastradas."""

    model = Turma
    template_name = "turmas/turma_lista.html"
    context_object_name = "turmas"
    titulo_pagina = "Turmas"
    breadcrumb_rotulo = "Turmas"
    breadcrumb_url = None


class TurmaCreateView(LoginRequiredMixin, SuccessMessageMixin, ViewComTituloEBreadcrumb, CreateView):
    """Cria uma nova turma."""

    model = Turma
    template_name = "turmas/turma_formulario.html"
    form_class = TurmaForm
    success_url = reverse_lazy("turmas:lista")
    success_message = "Turma cadastrada com sucesso!"
    titulo_pagina = "Cadastrar turma"
    breadcrumb_rotulo = "Nova turma"
    breadcrumb_pai = (("Turmas", reverse_lazy("turmas:lista")),)


class TurmaUpdateView(LoginRequiredMixin, SuccessMessageMixin, ViewComTituloEBreadcrumb, UpdateView):
    """Atualiza uma turma."""

    model = Turma
    template_name = "turmas/turma_formulario.html"
    form_class = TurmaForm
    success_url = reverse_lazy("turmas:lista")
    success_message = "Turma atualizada com sucesso!"
    titulo_pagina = "Editar turma"
    breadcrumb_rotulo = "Editar turma"
    breadcrumb_pai = (("Turmas", reverse_lazy("turmas:lista")),)


class TurmaDeleteView(LoginRequiredMixin, ViewComTituloEBreadcrumb, DeleteView):
    """Remove uma turma."""

    model = Turma
    template_name = "turmas/turma_confirmar_exclusao.html"
    success_url = reverse_lazy("turmas:lista")
    titulo_pagina = "Excluir turma"
    breadcrumb_rotulo = "Excluir turma"
    breadcrumb_pai = (("Turmas", reverse_lazy("turmas:lista")),)

    def delete(self, request: Any, *args: Any, **kwargs: Any) -> Any:  # type: ignore[override]
        """Remove a turma com feedback ao usuário."""

        messages.success(request, "Turma removida com sucesso!")
        return super().delete(request, *args, **kwargs)
