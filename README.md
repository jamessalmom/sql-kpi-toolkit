# sql-kpi-toolkit

Parameterized, Jinja2-templated SQL for KPIs that show up in almost every
commercial/financial dashboard: **Pareto 80/20** client concentration,
**year-over-year variation**, and **goal attainment** by unit or
consultant. Targets Postgres-style SQL (window functions, CTEs) but reads
close enough to ANSI SQL to adapt to SQL Server / MySQL with minor tweaks.

Extracted from KPI engines built for executive BI portals (Chart.js /
Power BI dashboards) where the same three calculations kept getting
rewritten per project.

## Why templates instead of an ORM

These are analytical, window-function-heavy queries — exactly the case
where hand-written SQL beats an ORM's query builder. Templating just
parameterizes table/column names so the same battle-tested query works
across schemas without copy-pasting and re-editing SQL by hand.

## Usage

```python
from sql_kpi_toolkit import render_query

sql = render_query(
    "pareto_80_20.sql.j2",
    table="sales",
    client_column="client_id",
    amount_column="amount",
    date_column="sold_at",
)
# sql is plain SQL text with named params (:period_start, :period_end)
# ready to run through your driver of choice (psycopg2, SQLAlchemy, pyodbc, ...)
```

## Included templates

| Template | KPI |
|---|---|
| `pareto_80_20.sql.j2` | Cumulative revenue share per client, ranked |
| `yoy_variation.sql.j2` | Year-over-year % variation, with optional grouping |
| `goal_attainment.sql.j2` | Actual vs. goal per entity, with achieved/near/below status |

## Development

```bash
pip install -r requirements.txt
pip install pytest ruff
pytest
ruff check .
```

## License

MIT — see [LICENSE](LICENSE).
