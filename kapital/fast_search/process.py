"""
OPTIONAL extra work on a report's result, in Python.

Most reports need nothing here: the SQL does the job. When it does not (divide by 100,
add a column, merge two columns, sort ...), write a function with the SAME NAME as the
.sql file. It gets:
    table   — the pandas table Oracle returned
    values  — the form values, e.g. {"startdate": date(2026, 1, 1), "siteid": "01234"}
and returns the table to show and to put in Excel.

No function for a report = the table is shown as Oracle returned it.
"""


def deals_period(table, values):
    """Example for sql/deals_period.sql: amounts are in tiyin → сум, biggest first."""
    if "Сумма" in table:
        table["Сумма"] = table["Сумма"] / 100
        table = table.sort_values("Сумма", ascending=False)
    return table
