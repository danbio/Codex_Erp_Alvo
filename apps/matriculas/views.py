"""Views responsáveis pelas matrículas."""

from __future__ import annotations

from typing import Any

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from apps.core.views import ViewComTituloEBreadcrumb
from apps.matriculas.forms import MatriculaForm
from apps.matriculas.models import Matricula


class MatriculaListView(LoginRequiredMixin, ViewComTituloEBreadcrumb, ListView):
    """Lista as matrículas cadastradas."""

    model = Matricula
    template_name = "matriculas/matricula_lista.html"
    context_object_name = "matriculas"
    titulo_pagina = "Matrículas"
    breadcrumb_rotulo = "Matrículas"
    breadcrumb_url = None


class MatriculaCreateView(LoginRequiredMixin, SuccessMessageMixin, ViewComTituloEBreadcrumb, CreateView):
    """Cria uma nova matrícula."""

    model = Matricula
    template_name = "matriculas/matricula_formulario.html"
    form_class = MatriculaForm
    success_url = reverse_lazy("matriculas:lista")
    success_message = "Matrícula registrada com sucesso!"
    titulo_pagina = "Registrar matrícula"
    breadcrumb_rotulo = "Nova matrícula"
    breadcrumb_pai = (("Matrículas", reverse_lazy("matriculas:lista")),)


class MatriculaUpdateView(LoginRequiredMixin, SuccessMessageMixin, ViewComTituloEBreadcrumb, UpdateView):
    """Atualiza uma matrícula existente."""

    model = Matricula
    template_name = "matriculas/matricula_formulario.html"
    form_class = MatriculaForm
    success_url = reverse_lazy("matriculas:lista")
    success_message = "Matrícula atualizada com sucesso!"
    titulo_pagina = "Editar matrícula"
    breadcrumb_rotulo = "Editar matrícula"
    breadcrumb_pai = (("Matrículas", reverse_lazy("matriculas:lista")),)


class MatriculaDeleteView(LoginRequiredMixin, ViewComTituloEBreadcrumb, DeleteView):
    """Exclui uma matrícula."""

    model = Matricula
    template_name = "matriculas/matricula_confirmar_exclusao.html"
    success_url = reverse_lazy("matriculas:lista")
    titulo_pagina = "Excluir matrícula"
    breadcrumb_rotulo = "Excluir matrícula"
    breadcrumb_pai = (("Matrículas", reverse_lazy("matriculas:lista")),)

    def delete(self, request: Any, *args: Any, **kwargs: Any) -> Any:  # type: ignore[override]
        """Remove a matrícula com mensagem de confirmação."""

        messages.success(request, "Matrícula removida com sucesso!")
        return super().delete(request, *args, **kwargs)
