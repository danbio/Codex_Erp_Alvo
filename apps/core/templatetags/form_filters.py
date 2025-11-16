"""Filtros auxiliares para personalizar widgets de formulários."""

from typing import Any

from django import template
from django.forms.boundfield import BoundField

register = template.Library()


@register.filter(name="add_css_class")
def add_css_class(field: BoundField, css_class: str) -> Any:
    """Renderiza o campo com classes CSS adicionais.

    Parameters
    ----------
    field: BoundField
        Campo do formulário já associado a um formulário.
    css_class: str
        Sequência com as classes CSS extras (ex.: "form-control").
    """
    if not hasattr(field, "field"):
        return field

    attrs = field.field.widget.attrs.copy()
    existing = attrs.get("class", "").strip()
    attrs["class"] = f"{existing} {css_class}".strip()
    return field.as_widget(attrs=attrs)
