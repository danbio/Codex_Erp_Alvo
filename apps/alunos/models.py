"""Modelos relacionados à gestão de alunos."""

from __future__ import annotations

from django.db import models


class Aluno(models.Model):
    """Representa um aluno matriculado na instituição."""

    nome: models.CharField[str, str] = models.CharField("Nome completo", max_length=150)
    email: models.EmailField[str, str] = models.EmailField("E-mail", unique=True)
    telefone: models.CharField[str, str] = models.CharField("Telefone", max_length=20)
    data_nascimento: models.DateField = models.DateField("Data de nascimento")
    documento: models.CharField[str, str] = models.CharField("Documento", max_length=20, unique=True)
    endereco: models.CharField[str, str] = models.CharField("Endereço", max_length=255)
    criado_em: models.DateTimeField = models.DateTimeField("Criado em", auto_now_add=True)
    atualizado_em: models.DateTimeField = models.DateTimeField("Atualizado em", auto_now=True)

    class Meta:
        ordering = ["nome"]
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"

    def __str__(self) -> str:
        """Retorna a representação textual do aluno."""

        return self.nome
