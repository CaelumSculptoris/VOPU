# Reproducibility and Data Conventions

## Directory conventions

- `data/raw/`: immutable instrument exports and source datasets.
- `data/processed/`: cleaned data generated from raw data.
- `simulations/`: model inputs, solver configurations, and output summaries.
- `experiments/`: protocols, sample records, and bench notes.
- `analysis/`: scripts, notebooks, figures, and reports.
- `reports/`: dated internal reports and publication drafts.

## Naming

Use `YYYY-MM-DD_sample-or-run_measurement_revision.ext`.

Examples:

```text
2026-09-22_core-001_transmission_r01.csv
2026-09-22_core-001_design_r03.json
2026-09-22_E01_loss-analysis_r01.md
```

## Minimum metadata

Every dataset must include sample ID, design revision, instrument, calibration state, units, acquisition settings, operator, date, and a link to the analysis that produced each figure or table.

## Model requirements

Record mesh size, boundary conditions, material model, wavelength, source definition, solver version, convergence criteria, and random seeds where applicable. Report sensitivity to mesh and parameter uncertainty for any headline result.

## Reporting requirements

Plots must show units, uncertainty or replicate count, and the operating range. Do not silently discard failed runs or outliers; document the rule before applying it.
