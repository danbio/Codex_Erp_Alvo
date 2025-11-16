"""Modelos relacionados às configurações gerais do sistema."""

from __future__ import annotations

from django.db import models


class ConfiguracaoEmpresa(models.Model):
    """Armazena os dados institucionais da empresa."""

    nome: models.CharField[str, str] = models.CharField("Nome da empresa", max_length=150)
    cnpj: models.CharField[str, str] = models.CharField("CNPJ", max_length=20, unique=True)
    email: models.EmailField[str, str] = models.EmailField("E-mail")
    telefone: models.CharField[str, str] = models.CharField("Telefone", max_length=20)
    endereco: models.CharField[str, str] = models.CharField("Endereço", max_length=255)
    logotipo: models.FileField = models.FileField("Logotipo", upload_to="logotipos/", blank=True)
    criado_em: models.DateTimeField = models.DateTimeField("Criado em", auto_now_add=True)
    atualizado_em: models.DateTimeField = models.DateTimeField("Atualizado em", auto_now=True)

    class Meta:
        verbose_name = "Configuração da empresa"
        verbose_name_plural = "Configurações da empresa"

    def __str__(self) -> str:
        """Retorna o nome da empresa."""

        return self.nome

    @classmethod
    def get_singular(cls) -> "ConfiguracaoEmpresa":
        """Obtém a instância única de configuração criando-a se necessário."""

        configuracao, _ = cls.objects.get_or_create(
            pk=1,
            defaults={
                "nome": "Alvo Gestão",
                "cnpj": "00.000.000/0000-00",
                "email": "contato@alvogestao.com",
                "telefone": "(00) 0000-0000",
                "endereco": "Endereço não informado",
            },
        )
        return configuracao
