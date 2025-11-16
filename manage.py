#!/usr/bin/env python
"""Utilitário de linha de comando para tarefas administrativas do Django."""

from __future__ import annotations

import os
import sys


def main() -> None:
    """Executa comandos administrativos do Django."""

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alvo_gestao.settings")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
