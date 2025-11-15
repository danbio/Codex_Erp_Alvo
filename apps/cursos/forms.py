"""Formulários do módulo de cursos."""

from __future__ import annotations

from django import forms

from apps.core.forms import FormularioBootstrapMixin
from apps.cursos.models import Curso


class CursoForm(FormularioBootstrapMixin, forms.ModelForm):
    """Formulário de cursos."""

    class Meta:
        model = Curso
        fields = ["nome", "descricao", "carga_horaria", "valor", "ativo"]
        widgets = {"descricao": forms.Textarea(attrs={"rows": 4})}
