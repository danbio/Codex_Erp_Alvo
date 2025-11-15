"""Administração do módulo financeiro."""

from __future__ import annotations

from django.contrib import admin

from apps.financeiro.models import Pagamento


@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    """Configuração do admin de pagamentos."""

    list_display = ("descricao", "matricula", "valor", "data_vencimento", "status")
    list_filter = ("status", "data_vencimento")
    search_fields = ("descricao", "matricula__aluno__nome")
