"""Ponto de entrada WSGI para o projeto Alvo Gestão."""

from __future__ import annotations

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alvo_gestao.settings")

application = get_wsgi_application()
