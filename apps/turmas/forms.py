"""Formulários relacionados às turmas."""

from __future__ import annotations

from django import forms

from apps.core.forms import FormularioBootstrapMixin
from apps.turmas.models import Turma


class TurmaForm(FormularioBootstrapMixin, forms.ModelForm):
    """Formulário para cadastro de turmas."""

    class Meta:
        model = Turma
        fields = [
            "nome",
            "curso",
            "professor",
            "data_inicio",
            "data_fim",
            "horario",
            "ativa",
        ]
        widgets = {
            "data_inicio": forms.DateInput(attrs={"type": "date"}),
            "data_fim": forms.DateInput(attrs={"type": "date"}),
        }
