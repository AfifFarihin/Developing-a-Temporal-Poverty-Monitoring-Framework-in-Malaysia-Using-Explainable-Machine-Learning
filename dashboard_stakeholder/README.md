# Malaysia Poverty Monitor - Stakeholder Dashboard

This Dash app is the stakeholder-facing version of the Malaysia state-level poverty monitoring dashboard. It supports government agencies, NGOs, researchers, development agencies, and community or policy advocates with plain-language guidance, transparent caveats, and state-level monitoring evidence.

## Run

From the source-code folder:

```powershell
.\.venv\Scripts\python.exe dashboard_stakeholder\app.py
```

Open `http://127.0.0.1:8051`.

## Tabs

| Tab | Purpose |
|---|---|
| Overview | Bottom-line reading of high-poverty states, survey trend fit, important model factors, and cautious stakeholder uses. |
| State Review | State-specific suggested use, trend comparison, supporting-indicator profile, and all-state comparison table. |
| Reliability Check | Plain-language model comparison, uncertainty, larger prediction gaps, and supporting-indicator relationships for research and agency review. |

## Certified Metrics

| Plain-language metric | Value |
|---|---:|
| Average prediction error | 2.52 pp |
| Large-error penalty | 4.56 pp |
| Pattern explained | 0.22 |
| Ranking agreement | 0.79 |

## Caveats

- Primary result: Malaysia state-level absolute poverty using the selected Random Forest model.
- Certified model outputs are exposed for absolute and relative poverty only; hardcore poverty is excluded because no certified LOSO model is submitted for that target.
- The dashboard is a monitoring support tool, not a replacement for official DOSM survey releases.
- The PNG files in `assets/` are documentation screenshots for the report/poster evidence chain; they are not rendered by the live Dash app.
- Model-factor charts are descriptive and should not be interpreted as causal proof.
- Relative poverty remains mainly year/trend driven and should not be presented as satellite-improved.
