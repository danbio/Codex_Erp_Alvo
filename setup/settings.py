"""Configurações principais do projeto Django."""

from __future__ import annotations

import os
from pathlib import Path

from django.core.exceptions import ImproperlyConfigured

BASE_DIR = Path(__file__).resolve().parent.parent


def carregar_variaveis_ambiente(arquivo_env: Path) -> None:
    """Popular ``os.environ`` com pares declarados em um arquivo ``.env``.

    A função lê o arquivo linha a linha, ignorando comentários, e mantém as
    variáveis já definidas no ambiente (prioridade para variáveis do sistema).
    Esse comportamento permite utilizar o mesmo código em diferentes cenários,
    evitando o hardcode de segredos sensíveis.
    """

    if not arquivo_env.exists():
        return

    for linha in arquivo_env.read_text(encoding="utf-8").splitlines():
        if not linha or linha.startswith("#"):
            continue
        if "=" not in linha:
            continue
        chave, valor = linha.split("=", maxsplit=1)
        os.environ.setdefault(chave.strip(), valor.strip())


carregar_variaveis_ambiente(BASE_DIR / ".env")


def obter_configuracao(chave: str, padrao: str | None = None, obrigatorio: bool = False) -> str:
    """Recupera valores de configuração, garantindo presença quando necessário."""

    valor = os.getenv(chave, padrao)
    if obrigatorio and not valor:
        raise ImproperlyConfigured(
            f"Defina a variável de ambiente '{chave}' antes de iniciar o servidor."
        )
    return valor

SECRET_KEY = obter_configuracao("DJANGO_SECRET_KEY", obrigatorio=True)

DEBUG = obter_configuracao("DJANGO_DEBUG", "False").lower() == "true"

ALLOWED_HOSTS = [
    host.strip()
    for host in obter_configuracao("DJANGO_ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")
    if host.strip()
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "setup.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "setup.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internacionalização
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True

# Configurações de arquivos estáticos
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

# Login Redirect
LOGIN_TEMPLATE_NAME = "registration/login.html"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "login"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
