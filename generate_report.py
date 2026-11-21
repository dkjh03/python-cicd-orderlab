from pathlib import Path

from orderlab.csv_report import revenue_from_csv

revenue = revenue_from_csv("data/sample_orders.csv")

site = Path("site")
site.mkdir(exist_ok=True)

(site / "index.html").write_text(
    f"""<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>OrderLab Report</title>
</head>
<body>
    <h1>OrderLab Report</h1>
    <p>Total revenue: {revenue:,} KRW</p>
</body>
</html>
""",
    encoding="utf-8",
)
