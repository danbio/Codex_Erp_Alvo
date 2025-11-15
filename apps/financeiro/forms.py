"""Formulários do módulo financeiro."""

from __future__ import annotations

from django import forms

from apps.core.forms import FormularioBootstrapMixin
from apps.financeiro.models import Pagamento


class PagamentoForm(FormularioBootstrapMixin, forms.ModelForm):
    """Formulário padrão para criação e edição de pagamentos."""

    class Meta:
        model = Pagamento
        fields = [
            "matricula",
            "descricao",
            "valor",
            "data_vencimento",
            "data_pagamento",
            "status",
            "observacoes",
        ]
        widgets = {
            "data_vencimento": forms.DateInput(attrs={"type": "date"}),
            "data_pagamento": forms.DateInput(attrs={"type": "date"}),
            "observacoes": forms.Textarea(attrs={"rows": 4}),
        }
