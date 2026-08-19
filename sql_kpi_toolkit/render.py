"""Renders the bundled .sql.j2 templates with the given parameters."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader, StrictUndefined

_TEMPLATES_DIR = Path(__file__).parent / "queries"

_env = Environment(
    loader=FileSystemLoader(str(_TEMPLATES_DIR)),
    undefined=StrictUndefined,
    trim_blocks=True,
    lstrip_blocks=True,
)


def render_query(template_name: str, **params: Any) -> str:
    """Render one of the bundled KPI query templates.

    Parameters
    ----------
    template_name:
        File name inside ``sql_kpi_toolkit/queries/`` (e.g. ``"pareto_80_20.sql.j2"``).
    **params:
        Values substituted into the template (table/column names, filters).
    """
    template = _env.get_template(template_name)
    return template.render(**params)


def list_templates() -> list[str]:
    return sorted(p.name for p in _TEMPLATES_DIR.glob("*.sql.j2"))
