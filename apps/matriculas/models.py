"""Modelos responsáveis pelas matrículas."""

from __future__ import annotations

from django.db import models

from apps.alunos.models import Aluno
from apps.turmas.models import Turma


class Matricula(models.Model):
    """Representa a matrícula de um aluno em uma turma."""

    class StatusMatricula(models.TextChoices):
        """Enumerador de status de matrícula."""

        ATIVA = "ativa", "Ativa"
        CONCLUIDA = "concluida", "Concluída"
        CANCELADA = "cancelada", "Cancelada"

    aluno: models.ForeignKey[Aluno, Aluno] = models.ForeignKey(
        Aluno,
        on_delete=models.PROTECT,
        related_name="matriculas",
        verbose_name="Aluno",
    )
    turma: models.ForeignKey[Turma, Turma] = models.ForeignKey(
        Turma,
        on_delete=models.PROTECT,
        related_name="matriculas",
        verbose_name="Turma",
    )
    data_matricula: models.DateField = models.DateField("Data da matrícula")
    status: models.CharField[str, str] = models.CharField(
        "Status",
        max_length=20,
        choices=StatusMatricula.choices,
        default=StatusMatricula.ATIVA,
    )
    observacoes: models.TextField = models.TextField("Observações", blank=True)
    criado_em: models.DateTimeField = models.DateTimeField("Criado em", auto_now_add=True)
    atualizado_em: models.DateTimeField = models.DateTimeField("Atualizado em", auto_now=True)

    class Meta:
        ordering = ["-data_matricula"]
        verbose_name = "Matrícula"
        verbose_name_plural = "Matrículas"
        unique_together = ("aluno", "turma")

    def __str__(self) -> str:
        """Retorna uma descrição resumida da matrícula."""

        return f"{self.aluno.nome} em {self.turma.nome}"
