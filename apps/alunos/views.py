"""Views responsáveis pelo fluxo de alunos."""

from __future__ import annotations

from typing import Any

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from apps.alunos.forms import AlunoForm
from apps.alunos.models import Aluno
from apps.core.views import ViewComTituloEBreadcrumb


class AlunoListView(LoginRequiredMixin, ViewComTituloEBreadcrumb, ListView):
    """Lista todos os alunos cadastrados."""

    model = Aluno
    template_name = "alunos/aluno_lista.html"
    context_object_name = "alunos"
    titulo_pagina = "Alunos"
    breadcrumb_rotulo = "Alunos"
    breadcrumb_url = None


class AlunoCreateView(LoginRequiredMixin, SuccessMessageMixin, ViewComTituloEBreadcrumb, CreateView):
    """Cria um novo aluno."""

    model = Aluno
    template_name = "alunos/aluno_formulario.html"
    form_class = AlunoForm
    success_url = reverse_lazy("alunos:lista")
    success_message = "Aluno criado com sucesso!"
    titulo_pagina = "Cadastrar aluno"
    breadcrumb_rotulo = "Novo aluno"
    breadcrumb_pai = (("Alunos", reverse_lazy("alunos:lista")),)


class AlunoUpdateView(LoginRequiredMixin, SuccessMessageMixin, ViewComTituloEBreadcrumb, UpdateView):
    """Atualiza os dados de um aluno."""

    model = Aluno
    template_name = "alunos/aluno_formulario.html"
    form_class = AlunoForm
    success_url = reverse_lazy("alunos:lista")
    success_message = "Aluno atualizado com sucesso!"
    titulo_pagina = "Editar aluno"
    breadcrumb_rotulo = "Editar aluno"
    breadcrumb_pai = (("Alunos", reverse_lazy("alunos:lista")),)


class AlunoDeleteView(LoginRequiredMixin, ViewComTituloEBreadcrumb, DeleteView):
    """Remove um aluno do cadastro."""

    model = Aluno
    template_name = "alunos/aluno_confirmar_exclusao.html"
    success_url = reverse_lazy("alunos:lista")
    titulo_pagina = "Excluir aluno"
    breadcrumb_rotulo = "Excluir aluno"
    breadcrumb_pai = (("Alunos", reverse_lazy("alunos:lista")),)

    def delete(self, request: Any, *args: Any, **kwargs: Any) -> Any:  # type: ignore[override]
        """Exclui o registro e informa o usuário."""

        messages.success(request, "Aluno removido com sucesso!")
        return super().delete(request, *args, **kwargs)
