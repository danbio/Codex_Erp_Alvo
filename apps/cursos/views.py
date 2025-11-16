"""Views do módulo de cursos."""

from __future__ import annotations

from typing import Any

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from apps.core.views import ViewComTituloEBreadcrumb
from apps.cursos.forms import CursoForm
from apps.cursos.models import Curso


class CursoListView(LoginRequiredMixin, ViewComTituloEBreadcrumb, ListView):
    """Lista os cursos disponíveis."""

    model = Curso
    template_name = "cursos/curso_lista.html"
    context_object_name = "cursos"
    titulo_pagina = "Cursos"
    breadcrumb_rotulo = "Cursos"
    breadcrumb_url = None


class CursoCreateView(LoginRequiredMixin, SuccessMessageMixin, ViewComTituloEBreadcrumb, CreateView):
    """Cadastra um novo curso."""

    model = Curso
    template_name = "cursos/curso_formulario.html"
    form_class = CursoForm
    success_url = reverse_lazy("cursos:lista")
    success_message = "Curso criado com sucesso!"
    titulo_pagina = "Cadastrar curso"
    breadcrumb_rotulo = "Novo curso"
    breadcrumb_pai = (("Cursos", reverse_lazy("cursos:lista")),)


class CursoUpdateView(LoginRequiredMixin, SuccessMessageMixin, ViewComTituloEBreadcrumb, UpdateView):
    """Edita um curso existente."""

    model = Curso
    template_name = "cursos/curso_formulario.html"
    form_class = CursoForm
    success_url = reverse_lazy("cursos:lista")
    success_message = "Curso atualizado com sucesso!"
    titulo_pagina = "Editar curso"
    breadcrumb_rotulo = "Editar curso"
    breadcrumb_pai = (("Cursos", reverse_lazy("cursos:lista")),)


class CursoDeleteView(LoginRequiredMixin, ViewComTituloEBreadcrumb, DeleteView):
    """Remove um curso."""

    model = Curso
    template_name = "cursos/curso_confirmar_exclusao.html"
    success_url = reverse_lazy("cursos:lista")
    titulo_pagina = "Excluir curso"
    breadcrumb_rotulo = "Excluir curso"
    breadcrumb_pai = (("Cursos", reverse_lazy("cursos:lista")),)

    def delete(self, request: Any, *args: Any, **kwargs: Any) -> Any:  # type: ignore[override]
        """Remove o curso exibindo mensagem ao usuário."""

        messages.success(request, "Curso removido com sucesso!")
        return super().delete(request, *args, **kwargs)
