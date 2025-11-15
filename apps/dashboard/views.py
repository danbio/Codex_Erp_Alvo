"""Views responsáveis pelo painel de controle do ERP."""

from __future__ import annotations

from typing import Any, Dict

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from apps.alunos.models import Aluno
from apps.core.views import ViewComTituloEBreadcrumb
from apps.cursos.models import Curso
from apps.financeiro.models import Pagamento
from apps.matriculas.models import Matricula
from apps.professores.models import Professor
from apps.turmas.models import Turma


class DashboardView(LoginRequiredMixin, ViewComTituloEBreadcrumb, TemplateView):
    """Exibe métricas gerais do sistema."""

    template_name = "dashboard/visao_geral.html"
    titulo_pagina = "Visão geral"
    breadcrumb_rotulo = "Dashboard"
    breadcrumb_url = None

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:  # type: ignore[override]
        """Adiciona métricas ao contexto do template."""

        contexto = super().get_context_data(**kwargs)
        contexto["total_alunos"] = Aluno.objects.count()
        contexto["total_professores"] = Professor.objects.count()
        contexto["total_cursos"] = Curso.objects.count()
        contexto["total_turmas_ativas"] = Turma.objects.filter(ativa=True).count()
        contexto["total_matriculas"] = Matricula.objects.count()
        contexto["total_pagamentos_pendentes"] = Pagamento.objects.filter(
            status=Pagamento.StatusPagamento.PENDENTE
        ).count()
        return contexto
