"""Modelos do módulo financeiro."""

from __future__ import annotations

from django.db import models

from apps.matriculas.models import Matricula


class Pagamento(models.Model):
    """Representa o pagamento relacionado a uma matrícula."""

    class StatusPagamento(models.TextChoices):
        """Status possíveis para um pagamento."""

        PENDENTE = "pendente", "Pendente"
        PAGO = "pago", "Pago"
        ATRASADO = "atrasado", "Atrasado"

    matricula: models.ForeignKey[Matricula, Matricula] = models.ForeignKey(
        Matricula,
        on_delete=models.CASCADE,
        related_name="pagamentos",
        verbose_name="Matrícula",
    )
    descricao: models.CharField[str, str] = models.CharField("Descrição", max_length=150)
    valor: models.DecimalField = models.DecimalField("Valor", max_digits=10, decimal_places=2)
    data_vencimento: models.DateField = models.DateField("Data de vencimento")
    data_pagamento: models.DateField = models.DateField("Data de pagamento", null=True, blank=True)
    status: models.CharField[str, str] = models.CharField(
        "Status",
        max_length=20,
        choices=StatusPagamento.choices,
        default=StatusPagamento.PENDENTE,
    )
    observacoes: models.TextField = models.TextField("Observações", blank=True)
    criado_em: models.DateTimeField = models.DateTimeField("Criado em", auto_now_add=True)
    atualizado_em: models.DateTimeField = models.DateTimeField("Atualizado em", auto_now=True)

    class Meta:
        ordering = ["status", "data_vencimento"]
        verbose_name = "Pagamento"
        verbose_name_plural = "Pagamentos"

    def __str__(self) -> str:
        """Retorna descrição do pagamento."""

        return f"{self.descricao} - {self.valor:,.2f}"
