"""Modelos relacionados aos professores."""

from __future__ import annotations

from django.db import models


class Professor(models.Model):
    """Representa um professor associado aos cursos."""

    nome: models.CharField[str, str] = models.CharField("Nome completo", max_length=150)
    email: models.EmailField[str, str] = models.EmailField("E-mail", unique=True)
    telefone: models.CharField[str, str] = models.CharField("Telefone", max_length=20)
    especialidade: models.CharField[str, str] = models.CharField("Especialidade", max_length=120)
    documento: models.CharField[str, str] = models.CharField("Documento", max_length=20, unique=True)
    ativo: models.BooleanField = models.BooleanField("Ativo", default=True)
    criado_em: models.DateTimeField = models.DateTimeField("Criado em", auto_now_add=True)
    atualizado_em: models.DateTimeField = models.DateTimeField("Atualizado em", auto_now=True)

    class Meta:
        ordering = ["nome"]
        verbose_name = "Professor"
        verbose_name_plural = "Professores"

    def __str__(self) -> str:
        """Retorna o nome do professor."""

        return self.nome
