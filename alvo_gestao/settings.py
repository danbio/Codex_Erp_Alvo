"""Configurações principais do projeto Alvo Gestão."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import dj_database_url
from dotenv import load_dotenv

BASE_DIR: Path = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

SECRET_KEY: str = os.getenv("SECRET_KEY", "chave-insegura-para-desenvolvimento")
DEBUG: bool = os.getenv("DEBUG", "True").lower() in {"1", "true", "sim"}

ALLOWED_HOSTS_RAW: str = os.getenv("ALLOWED_HOSTS", "")
ALLOWED_HOSTS: list[str] = [host.strip() for host in ALLOWED_HOSTS_RAW.split(",") if host.strip()]

INSTALLED_APPS: list[str] = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "apps.alunos.apps.AlunosConfig",
    "apps.professores.apps.ProfessoresConfig",
    "apps.cursos.apps.CursosConfig",
    "apps.turmas.apps.TurmasConfig",
    "apps.matriculas.apps.MatriculasConfig",
    "apps.financeiro.apps.FinanceiroConfig",
    "apps.dashboard.apps.DashboardConfig",
    "apps.configuracoes.apps.ConfiguracoesConfig",
]

MIDDLEWARE: list[str] = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF: str = "alvo_gestao.urls"

TEMPLATES: list[dict[str, Any]] = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    }
]

WSGI_APPLICATION: str = "alvo_gestao.wsgi.application"

DATABASE_URL: str = os.getenv("DATABASE_URL", f"sqlite:///{BASE_DIR / 'db.sqlite3'}")
DATABASES: dict[str, dict[str, Any]] = {
    "default": dj_database_url.parse(DATABASE_URL, conn_max_age=600, ssl_require=not DEBUG),
}

AUTH_PASSWORD_VALIDATORS: list[dict[str, str]] = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE: str = "pt-br"
TIME_ZONE: str = "America/Sao_Paulo"
USE_I18N: bool = True
USE_TZ: bool = True

STATIC_URL: str = "static/"
STATIC_ROOT: Path = BASE_DIR / "staticfiles"
STATICFILES_DIRS: list[Path] = [BASE_DIR / "static"]

MEDIA_URL: str = "media/"
MEDIA_ROOT: Path = BASE_DIR / "media"

DEFAULT_AUTO_FIELD: str = "django.db.models.BigAutoField"

LOGIN_URL: str = "login"
LOGIN_REDIRECT_URL: str = "dashboard:visao_geral"
LOGOUT_REDIRECT_URL: str = "login"

EMAIL_BACKEND: str = "django.core.mail.backends.console.EmailBackend"

CSRF_TRUSTED_ORIGINS: list[str] = [origem for origem in os.getenv("CSRF_TRUSTED_ORIGINS", "").split(",") if origem]
