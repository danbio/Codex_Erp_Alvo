"""Formulários referentes aos professores."""

from __future__ import annotations

from django import forms

from apps.core.forms import FormularioBootstrapMixin
from apps.professores.models import Professor


class ProfessorForm(FormularioBootstrapMixin, forms.ModelForm):
    """Formulário para criação e edição de professores."""

    class Meta:
        model = Professor
        fields = ["nome", "email", "telefone", "especialidade", "documento", "ativo"]
