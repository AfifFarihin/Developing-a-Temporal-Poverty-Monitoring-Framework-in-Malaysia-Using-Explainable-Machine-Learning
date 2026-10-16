# Submission Run Guide

## Environment

From the source-code folder `Muhammad Afif Farihin Bin Mohammad-TP076690-APD3F2509CS(DA)-Source Code`:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install --prefer-binary -r setup\requirements-base.txt
```

The environment folder is local only. Do not include `.venv/` in the submission package.

## Run The Notebooks Manually

Open the notebooks in VS Code or Jupyter and run them in this order:

1. `notebooks/00_dosm_raw_to_labels.ipynb`
2. `notebooks/01_malaysia_data_preparation.ipynb`
3. `notebooks/02_malaysia_spatial_features.ipynb`
4. `notebooks/03_model_training_evaluation.ipynb`
5. `notebooks/04_dashboard_artifacts.ipynb`

The workflow is Malaysia state-level only. Notebook 00 retains the official DOSM raw state poverty file under `data/raw/dosm/`, writes cleaned DOSM labels under `data/interim/`, and validates those labels against the retained model-ready panel. The later notebooks write state-level metrics, figures, and dashboard artifacts under `outputs/metrics/`, `outputs/figures/`, and `outputs/qa/`. The `outputs/qa/` folder contains pre-shipped quality-assurance summaries from the latest validated pipeline run; it is also regenerated when notebooks 03 and 04 are re-executed.

## Dashboard

Install the dashboard requirements if needed:

```powershell
.\.venv\Scripts\python.exe -m pip install -r dashboard_stakeholder\requirements.txt
```

Run the submitted stakeholder dashboard:

```powershell
.\.venv\Scripts\python.exe dashboard_stakeholder\app.py
```

Open `http://127.0.0.1:8051` and review the Overview, State Review, and Reliability Check tabs.

## Reproducibility Notes

- Final extracted state-level input files are included under `data/`.
- The official DOSM raw state poverty file is retained at `data/raw/dosm/hh_poverty_state.csv`, and the cleaned project-year labels are retained at `data/interim/dosm_poverty_state_clean.csv`.
- Google Earth Engine extraction is not required to inspect or rerun the final notebooks.
- If Earth Engine extraction scripts are used outside the submission package, copy `setup/local_reproducibility_config.example.env` to a local `.env` file and update the Earth Engine project/credential values.
- Certified headline metrics are recorded in `outputs/metrics/malaysia_state_model_comparison.csv`.
- `data/state_model_predictions.csv` is a generated selected-model prediction artifact created by Notebook 03. It is pre-shipped and can be used directly; if regenerating from scratch, run notebooks in order 00-01-02-03-04.

### Random Forest vs XGBoost reproducibility

The selected Random Forest absolute-poverty headline result is fully reproducible across reruns on the same OS, Python, and pinned package versions (Windows 11, Python 3.11, `xgboost==2.0.3`, `scikit-learn` pinned in `setup/requirements-base.txt`):

- RF (selected) — Absolute poverty: MAE = 2.524 pp, RMSE = 4.564, R² = 0.218, Spearman = 0.787.
- RF sensor-safe — Absolute poverty lower-error robustness benchmark: MAE = 2.362 pp, RMSE = 4.243, R² = 0.324, Spearman = 0.806.

XGBoost is reported as a comparator only. The XGBoost comparator was rerun in this submission cycle and the report (Table 7 / "Table 7 State-Level LOSO Cross-Validation Results", Section 5 body text) reflects the regenerated values:

- XGBoost full — Absolute poverty rank comparator: MAE = 2.414 pp, RMSE = 4.489, R² = 0.244, Spearman = 0.823.

XGBoost comparator metrics may still drift by small amounts (≤ ~0.07 pp MAE, ≤ ~0.04 R²) across different operating systems, BLAS implementations, or XGBoost binary builds, even with `random_state=42`, `n_jobs=1`, and `tree_method="hist"`. This affects only the comparator narrative; the selected Random Forest result and the relative-poverty year-only-baseline selection are not affected.
