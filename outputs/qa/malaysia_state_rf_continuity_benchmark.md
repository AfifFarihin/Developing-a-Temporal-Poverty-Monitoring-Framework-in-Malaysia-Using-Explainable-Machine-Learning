# Malaysia State Random Forest Continuity Benchmark

Purpose: document the Semester 1 Random Forest modelling plan inside the notebook-first final pipeline and record the manual state-level promotion decision.

Continuity facts:

- Part 1 proposed Random Forest as the Semester 2 non-parametric modelling direction.
- No retained executable old Random Forest modelling script is present in the final package.
- Random Forest has therefore been reimplemented as a Malaysia state-level benchmark in `notebooks/03_model_training_evaluation.ipynb` inside this notebook.
- Scope is state-level only. Only Malaysia state-level modelling forms part of the active submission.
- Random Forest was manually reviewed after notebook execution; it is selected only for the primary Malaysia state-level `poverty_absolute` point prediction.

Promotion status:

- Selected absolute-poverty point predictor: `rf_current_full`.
- Best observed absolute-poverty model in this run: `rf_sensor_safe`.
- Manual promotion review status: `completed_after_review`.
- RF is not claimed as decisively superior because the paired MAE uncertainty interval overlaps zero.
- Relative poverty is best handled as year/trend-driven because the year-only baseline has the strongest state-level metrics.

RF and state headline benchmark comparison:

| target | model | feature_policy | feature_count | loso_mae_pp | loso_rmse | loso_r2 | loso_spearman |
| --- | --- | --- | --- | --- | --- | --- | --- |
| poverty_absolute | rf_sensor_safe | sensor_safe | 10 | 2.3618 | 4.2432 | 0.3242 | 0.8060 |
| poverty_absolute | current_xgb | current_full | 21 | 2.4144 | 4.4891 | 0.2436 | 0.8229 |
| poverty_absolute | rf_current_full | current_full | 21 | 2.5242 | 4.5635 | 0.2183 | 0.7872 |
| poverty_absolute | year_only_xgb | year_only | 1 | 2.9614 | 4.8464 | 0.1184 | 0.4915 |
| poverty_relative | year_only_xgb | year_only | 1 | 2.2398 | 2.8919 | 0.2458 | 0.4284 |
| poverty_relative | rf_sensor_safe | sensor_safe | 10 | 2.5446 | 3.3348 | -0.0029 | 0.3904 |
| poverty_relative | current_xgb | current_full | 21 | 2.5469 | 3.2928 | 0.0222 | 0.4265 |
| poverty_relative | rf_current_full | current_full | 21 | 2.6328 | 3.4053 | -0.0458 | 0.3673 |

RF uncertainty intervals:

| target | model | metric | observed | ci_lower | ci_upper | n_boot | n_groups |
| --- | --- | --- | --- | --- | --- | --- | --- |
| poverty_absolute | rf_current_full | mae | 2.5242 | 1.5874 | 3.8606 | 200 | 16 |
| poverty_absolute | rf_current_full | pearson | 0.5092 | 0.3337 | 0.8175 | 200 | 16 |
| poverty_absolute | rf_current_full | r2 | 0.2183 | -0.0916 | 0.6067 | 200 | 16 |
| poverty_absolute | rf_current_full | rmse | 4.5635 | 2.3355 | 6.5276 | 200 | 16 |
| poverty_absolute | rf_current_full | spearman | 0.7872 | 0.6745 | 0.8720 | 200 | 16 |
| poverty_absolute | rf_sensor_safe | mae | 2.3618 | 1.4042 | 3.5808 | 200 | 16 |
| poverty_absolute | rf_sensor_safe | pearson | 0.5965 | 0.4578 | 0.8235 | 200 | 16 |
| poverty_absolute | rf_sensor_safe | r2 | 0.3242 | 0.0274 | 0.6390 | 200 | 16 |
| poverty_absolute | rf_sensor_safe | rmse | 4.2432 | 2.0813 | 5.9686 | 200 | 16 |
| poverty_absolute | rf_sensor_safe | spearman | 0.8060 | 0.6928 | 0.8853 | 200 | 16 |
| poverty_relative | rf_current_full | mae | 2.6328 | 2.1234 | 3.2587 | 200 | 16 |
| poverty_relative | rf_current_full | pearson | 0.3295 | 0.2115 | 0.5210 | 200 | 16 |
| poverty_relative | rf_current_full | r2 | -0.0458 | -0.3763 | 0.1886 | 200 | 16 |
| poverty_relative | rf_current_full | rmse | 3.4053 | 2.8126 | 4.0733 | 200 | 16 |
| poverty_relative | rf_current_full | spearman | 0.3673 | 0.2177 | 0.5231 | 200 | 16 |
| poverty_relative | rf_sensor_safe | mae | 2.5446 | 2.0759 | 3.1213 | 200 | 16 |
| poverty_relative | rf_sensor_safe | pearson | 0.3556 | 0.2263 | 0.5339 | 200 | 16 |
| poverty_relative | rf_sensor_safe | r2 | -0.0029 | -0.3140 | 0.2309 | 200 | 16 |
| poverty_relative | rf_sensor_safe | rmse | 3.3348 | 2.7741 | 3.9741 | 200 | 16 |
| poverty_relative | rf_sensor_safe | spearman | 0.3904 | 0.2214 | 0.5389 | 200 | 16 |
