"""sql_kpi_toolkit

Reusable, Jinja2-templated SQL for common commercial/financial KPIs:
Pareto 80/20 client concentration, year-over-year variation, and goal
attainment by unit/consultant. Templates target Postgres-style SQL
(window functions, CTEs) but are close to ANSI SQL and easy to adapt.

This package renders parameterized SQL text; it does not execute queries
itself, so it has no database driver dependency.
"""

from .render import render_query

__all__ = ["render_query"]
__version__ = "0.1.0"
