"""Testes das views públicas e autenticadas."""

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class PaginaInicialViewTests(TestCase):
    """Garante que a página inicial permanece acessível."""

    def test_homepage_renderiza_com_sucesso(self) -> None:
        resposta = self.client.get(reverse("home"))
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, "Bem-vindo")


class DashboardViewTests(TestCase):
    """Valida as restrições de autenticação do dashboard."""

    def setUp(self) -> None:
        usuario_modelo = get_user_model()
        self.usuario = usuario_modelo.objects.create_user(
            username="usuario_teste",
            password="senha_segura123",
            email="teste@example.com",
        )

    def test_dashboard_exige_autenticacao(self) -> None:
        resposta = self.client.get(reverse("dashboard"))
        self.assertEqual(resposta.status_code, 302)
        self.assertIn(reverse("login"), resposta.url)

    def test_dashboard_autenticado(self) -> None:
        self.client.login(username="usuario_teste", password="senha_segura123")
        resposta = self.client.get(reverse("dashboard"))
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, "Dashboard")
