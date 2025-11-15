"""Formulários de matrículas."""

from __future__ import annotations

from django import forms

from apps.core.forms import FormularioBootstrapMixin
from apps.matriculas.models import Matricula


class MatriculaForm(FormularioBootstrapMixin, forms.ModelForm):
    """Formulário padrão de matrículas."""

    class Meta:
        model = Matricula
        fields = ["aluno", "turma", "data_matricula", "status", "observacoes"]
        widgets = {
            "data_matricula": forms.DateInput(attrs={"type": "date"}),
            "observacoes": forms.Textarea(attrs={"rows": 4}),
        }
