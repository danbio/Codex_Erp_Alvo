"""Formulários do módulo de configurações."""

from __future__ import annotations

from django import forms

from apps.configuracoes.models import ConfiguracaoEmpresa
from apps.core.forms import FormularioBootstrapMixin


class ConfiguracaoEmpresaForm(FormularioBootstrapMixin, forms.ModelForm):
    """Formulário para atualizar os dados da empresa."""

    class Meta:
        model = ConfiguracaoEmpresa
        fields = ["nome", "cnpj", "email", "telefone", "endereco", "logotipo"]
