"""Componentes compartilhados para formulários do projeto."""

from __future__ import annotations

from typing import Any

from django import forms


class FormularioBootstrapMixin:
    """Adiciona classes do Bootstrap 5 aos widgets de um formulário."""

    def _aplicar_estilos_bootstrap(self) -> None:
        for campo in self.fields.values():  # type: ignore[attr-defined]
            widget: forms.Widget = campo.widget
            classes_existentes: set[str] = set(widget.attrs.get("class", "").split())
            if isinstance(widget, forms.CheckboxInput):
                classes_existentes.update({"form-check-input"})
                classes_existentes.discard("form-control")
            else:
                classes_existentes.add("form-control")
            widget.attrs["class"] = " ".join(sorted(filter(None, classes_existentes)))

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # noqa: D401 - delega para super
        super().__init__(*args, **kwargs)  # type: ignore[misc]
        self._aplicar_estilos_bootstrap()
