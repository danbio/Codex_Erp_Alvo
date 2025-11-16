"""Formulários para manipulação de alunos."""

from __future__ import annotations

from django import forms

from apps.alunos.models import Aluno
from apps.core.forms import FormularioBootstrapMixin


class AlunoForm(FormularioBootstrapMixin, forms.ModelForm):
    """Formulário padrão para criação e edição de alunos."""

    class Meta:
        model = Aluno
        fields = [
            "nome",
            "email",
            "telefone",
            "data_nascimento",
            "documento",
            "endereco",
        ]
        widgets = {
            "data_nascimento": forms.DateInput(attrs={"type": "date"}),
        }
