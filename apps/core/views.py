"""Utilitários para views baseadas em classe."""

from __future__ import annotations

from typing import Any, Iterable

from django.http import HttpRequest


class BreadcrumbMixin:
    """Fornece contexto de breadcrumbs para templates."""

    breadcrumb_rotulo: str = ""
    breadcrumb_url: str | None = None
    breadcrumb_pai: Iterable[tuple[str, str | None]] = ()

    def get_breadcrumbs(self) -> list[tuple[str, str | None]]:
        breadcrumbs: list[tuple[str, str | None]] = list(self.breadcrumb_pai)
        breadcrumbs.append((self.breadcrumb_rotulo, self.breadcrumb_url))
        return breadcrumbs

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:  # type: ignore[override]
        contexto: dict[str, Any] = super().get_context_data(**kwargs)  # type: ignore[misc]
        contexto["breadcrumbs"] = self.get_breadcrumbs()
        return contexto


class TituloPaginaMixin:
    """Define um título padrão para utilização no template base."""

    titulo_pagina: str = ""

    def get_titulo_pagina(self) -> str:
        return self.titulo_pagina

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:  # type: ignore[override]
        contexto: dict[str, Any] = super().get_context_data(**kwargs)  # type: ignore[misc]
        contexto["titulo_pagina"] = self.get_titulo_pagina()
        return contexto


class ViewComTituloEBreadcrumb(TituloPaginaMixin, BreadcrumbMixin):
    """Combina mixins de título e breadcrumb."""

    request: HttpRequest
