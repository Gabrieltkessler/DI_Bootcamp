"""
insights_server.py
-------------------
Your own MCP server for the Smart Data Scout project.

It exposes data-analysis tools that the third-party filesystem/fetch
servers can't do on their own: statistical summaries, correlation,
outlier detection, and markdown report writing.

Run standalone for a quick smoke test:
    python insights_server.py
(it will then wait on stdio, which is expected -- it's meant to be
spawned by the MCP client, not run interactively)
"""
import json
import os

import pandas as pd
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("insights")

DATA_DIR = os.environ.get("DATA_DIR", "./data")


def _resolve(path: str) -> str:
    """Keep file access inside DATA_DIR (basic safety, mirrors what
    the filesystem server would enforce)."""
    full = os.path.abspath(os.path.join(DATA_DIR, os.path.basename(path)))
    return full


@mcp.tool()
def describe_csv(file_path: str) -> str:
    """Load a CSV file and return shape, column dtypes, summary
    statistics (describe()), and missing-value counts as JSON.

    Args:
        file_path: filename of the CSV inside the data directory
            (e.g. 'sales.csv'). Just the filename, not a full path.
    """
    path = _resolve(file_path)
    if not os.path.exists(path):
        return json.dumps({"error": f"File not found: {file_path}"})

    df = pd.read_csv(path)
    result = {
        "shape": {"rows": df.shape[0], "columns": df.shape[1]},
        "dtypes": {c: str(t) for c, t in df.dtypes.items()},
        "missing_values": df.isnull().sum().to_dict(),
        "describe": json.loads(df.describe(include="all").fillna("").to_json()),
    }
    return json.dumps(result, default=str)


@mcp.tool()
def correlate_columns(file_path: str, col_a: str, col_b: str) -> str:
    """Compute the Pearson correlation between two numeric columns
    in a CSV file.

    Args:
        file_path: filename of the CSV inside the data directory
        col_a: first numeric column name
        col_b: second numeric column name
    """
    path = _resolve(file_path)
    if not os.path.exists(path):
        return json.dumps({"error": f"File not found: {file_path}"})

    df = pd.read_csv(path)
    for col in (col_a, col_b):
        if col not in df.columns:
            return json.dumps({"error": f"Column not found: {col}"})

    corr = df[col_a].corr(df[col_b])
    if pd.isna(corr):
        return json.dumps({"error": "Correlation undefined (non-numeric or constant column)"})
    return json.dumps({"col_a": col_a, "col_b": col_b, "pearson_correlation": round(float(corr), 4)})


@mcp.tool()
def detect_outliers(file_path: str, column: str, z_thresh: float = 3.0) -> str:
    """Detect outliers in a numeric column using a z-score threshold.

    Args:
        file_path: filename of the CSV inside the data directory
        column: numeric column to check for outliers
        z_thresh: z-score cutoff, default 3.0
    """
    path = _resolve(file_path)
    if not os.path.exists(path):
        return json.dumps({"error": f"File not found: {file_path}"})

    df = pd.read_csv(path)
    if column not in df.columns:
        return json.dumps({"error": f"Column not found: {column}"})

    series = pd.to_numeric(df[column], errors="coerce")
    mean, std = series.mean(), series.std()
    if std == 0 or pd.isna(std):
        return json.dumps({"outlier_count": 0, "outlier_rows": []})

    z_scores = (series - mean) / std
    outlier_mask = z_scores.abs() > z_thresh
    outlier_rows = df[outlier_mask].head(20).to_dict(orient="records")

    return json.dumps({
        "outlier_count": int(outlier_mask.sum()),
        "z_thresh": z_thresh,
        "outlier_rows": outlier_rows,
    }, default=str)


@mcp.tool()
def write_markdown_report(filename: str, content: str) -> str:
    """Write markdown content to a report file inside the data directory.

    Args:
        filename: name of the report file, e.g. 'report.md'
        content: the markdown text to write
    """
    if not filename.endswith(".md"):
        filename += ".md"
    path = _resolve(filename)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return json.dumps({"status": "written", "path": path, "bytes": len(content)})


if __name__ == "__main__":
    mcp.run()
