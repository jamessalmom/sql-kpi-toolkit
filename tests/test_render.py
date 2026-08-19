import pytest
from jinja2 import UndefinedError

from sql_kpi_toolkit.render import list_templates, render_query


def test_lists_bundled_templates():
    templates = list_templates()
    assert "pareto_80_20.sql.j2" in templates
    assert "yoy_variation.sql.j2" in templates
    assert "goal_attainment.sql.j2" in templates


def test_renders_pareto_query_with_table_and_columns():
    sql = render_query(
        "pareto_80_20.sql.j2",
        table="sales",
        client_column="client_id",
        amount_column="amount",
        date_column="sold_at",
    )
    assert "FROM sales" in sql
    assert "client_id" in sql
    assert "cumulative_share_pct" in sql


def test_yoy_query_supports_optional_group_by():
    sql_grouped = render_query(
        "yoy_variation.sql.j2",
        table="sales",
        amount_column="amount",
        date_column="sold_at",
        group_by_column="region",
    )
    assert "PARTITION BY group_key" in sql_grouped

    sql_ungrouped = render_query(
        "yoy_variation.sql.j2",
        table="sales",
        amount_column="amount",
        date_column="sold_at",
        group_by_column=None,
    )
    assert "PARTITION BY" not in sql_ungrouped


def test_missing_required_param_raises():
    with pytest.raises(UndefinedError):
        render_query("pareto_80_20.sql.j2", table="sales")
