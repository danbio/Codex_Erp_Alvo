"""Modelos relacionados às turmas."""

from __future__ import annotations

from django.db import models

from apps.cursos.models import Curso
from apps.professores.models import Professor


class Turma(models.Model):
    """Representa uma turma associada a um curso e professor."""

    nome: models.CharField[str, str] = models.CharField("Nome", max_length=120)
    curso: models.ForeignKey[Curso, Curso] = models.ForeignKey(
        Curso,
        on_delete=models.PROTECT,
        related_name="turmas",
        verbose_name="Curso",
    )
    professor: models.ForeignKey[Professor, Professor] = models.ForeignKey(
        Professor,
        on_delete=models.PROTECT,
        related_name="turmas",
        verbose_name="Professor",
    )
    data_inicio: models.DateField = models.DateField("Data de início")
    data_fim: models.DateField = models.DateField("Data de término", null=True, blank=True)
    horario: models.CharField[str, str] = models.CharField("Horário", max_length=100)
    ativa: models.BooleanField = models.BooleanField("Ativa", default=True)
    criado_em: models.DateTimeField = models.DateTimeField("Criado em", auto_now_add=True)
    atualizado_em: models.DateTimeField = models.DateTimeField("Atualizado em", auto_now=True)

    class Meta:
        ordering = ["nome"]
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"

    def __str__(self) -> str:
        """Retorna a identificação da turma."""

        return f"{self.nome} - {self.curso.nome}"
