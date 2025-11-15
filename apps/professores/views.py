"""Views do módulo de professores."""

from __future__ import annotations

from typing import Any

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from apps.core.views import ViewComTituloEBreadcrumb
from apps.professores.forms import ProfessorForm
from apps.professores.models import Professor


class ProfessorListView(LoginRequiredMixin, ViewComTituloEBreadcrumb, ListView):
    """Exibe os professores cadastrados."""

    model = Professor
    template_name = "professores/professor_lista.html"
    context_object_name = "professores"
    titulo_pagina = "Professores"
    breadcrumb_rotulo = "Professores"
    breadcrumb_url = None


class ProfessorCreateView(LoginRequiredMixin, SuccessMessageMixin, ViewComTituloEBreadcrumb, CreateView):
    """Cria um novo professor."""

    model = Professor
    form_class = ProfessorForm
    template_name = "professores/professor_formulario.html"
    success_url = reverse_lazy("professores:lista")
    success_message = "Professor cadastrado com sucesso!"
    titulo_pagina = "Cadastrar professor"
    breadcrumb_rotulo = "Novo professor"
    breadcrumb_pai = (("Professores", reverse_lazy("professores:lista")),)


class ProfessorUpdateView(LoginRequiredMixin, SuccessMessageMixin, ViewComTituloEBreadcrumb, UpdateView):
    """Atualiza um professor existente."""

    model = Professor
    form_class = ProfessorForm
    template_name = "professores/professor_formulario.html"
    success_url = reverse_lazy("professores:lista")
    success_message = "Professor atualizado com sucesso!"
    titulo_pagina = "Editar professor"
    breadcrumb_rotulo = "Editar professor"
    breadcrumb_pai = (("Professores", reverse_lazy("professores:lista")),)


class ProfessorDeleteView(LoginRequiredMixin, ViewComTituloEBreadcrumb, DeleteView):
    """Exclui um professor."""

    model = Professor
    template_name = "professores/professor_confirmar_exclusao.html"
    success_url = reverse_lazy("professores:lista")
    titulo_pagina = "Excluir professor"
    breadcrumb_rotulo = "Excluir professor"
    breadcrumb_pai = (("Professores", reverse_lazy("professores:lista")),)

    def delete(self, request: Any, *args: Any, **kwargs: Any) -> Any:  # type: ignore[override]
        """Executa a exclusão com mensagem de feedback."""

        messages.success(request, "Professor removido com sucesso!")
        return super().delete(request, *args, **kwargs)
