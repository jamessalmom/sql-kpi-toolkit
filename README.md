# sql-kpi-toolkit

Jinja2 templates for three SQL calculations that show up in almost every commercial or financial dashboard: Pareto 80/20 client concentration, year-over-year variation and goal attainment per unit or consultant. The SQL is written for PostgreSQL (window functions and CTEs) and needs only small changes for SQL Server or MySQL.

I kept rewriting these three queries for each new BI portal, with different table and column names every time. The templates only parameterize those names; the query logic stays the same.

## Why templates instead of an ORM

These are analytical queries built on window functions, which is where hand-written SQL is clearer than an ORM query builder. Templating keeps one version of each query that works across schemas.

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
# plain SQL with named params (:period_start, :period_end),
# ready for psycopg2, SQLAlchemy, pyodbc or any other driver
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

MIT, see [LICENSE](LICENSE).
