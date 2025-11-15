"""Modelos do módulo de cursos."""

from __future__ import annotations

from django.db import models


class Curso(models.Model):
    """Representa um curso oferecido pela instituição."""

    nome: models.CharField[str, str] = models.CharField("Nome", max_length=150)
    descricao: models.TextField = models.TextField("Descrição", blank=True)
    carga_horaria: models.PositiveIntegerField = models.PositiveIntegerField("Carga horária (h)")
    valor: models.DecimalField = models.DecimalField("Valor", max_digits=10, decimal_places=2)
    ativo: models.BooleanField = models.BooleanField("Ativo", default=True)
    criado_em: models.DateTimeField = models.DateTimeField("Criado em", auto_now_add=True)
    atualizado_em: models.DateTimeField = models.DateTimeField("Atualizado em", auto_now=True)

    class Meta:
        ordering = ["nome"]
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self) -> str:
        """Retorna o nome do curso."""

        return self.nome
