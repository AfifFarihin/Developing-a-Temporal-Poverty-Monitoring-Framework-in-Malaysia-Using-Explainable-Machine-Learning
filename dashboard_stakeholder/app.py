"""
Malaysia Poverty Monitoring - stakeholder Dash dashboard.
Run from source-code folder: python dashboard_stakeholder/app.py
Opens at http://127.0.0.1:8051
"""
from __future__ import annotations

import sys
from pathlib import Path

# Allow sibling imports (data, charts, layout, callbacks)
sys.path.insert(0, str(Path(__file__).resolve().parent))

import dash_bootstrap_components as dbc
from dash import Dash

DASH_DIR   = Path(__file__).resolve().parent
ASSETS_DIR = DASH_DIR / "assets"

app = Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
    ],
    title="Malaysia Poverty Monitor - Stakeholder View",
    assets_folder=str(ASSETS_DIR),
    suppress_callback_exceptions=True,
)

# Import layout and callbacks after app is created
from layout import create_layout      # noqa: E402
from callbacks import register_callbacks  # noqa: E402

app.layout = create_layout()
register_callbacks()

if __name__ == "__main__":
    print("Starting Malaysia Poverty Monitor stakeholder dashboard...")
    print("Open http://127.0.0.1:8051 in your browser.")
    print("Press Ctrl+C to stop.\n")
    app.run(debug=False, dev_tools_ui=False, port=8051)
