# Experimental Work

This folder contains protocols, sample records, measurement plans, and bench notes. Start with the experiments in [`../docs/EXPERIMENT_MATRIX.md`](../docs/EXPERIMENT_MATRIX.md).

## First protocol package

- E01: straight-guide transparency (fiber-like propagation validation).
- E02: bend, spacing, and crosstalk tolerance.
- E03: terminal-node directed scattering pattern and efficiency calibration.
- E08: coupling and alignment tolerance.

Nonlinear tests should begin only after the linear reference paths and measurement calibration are stable. Any work involving lasers, dopants, nanoparticles, solvents, or supercritical CO2 requires appropriate safety procedures and facility approval.

## Key experimental principles

1. **Measure channel transparency** — confirm fiber-like propagation loss in fabricated VOPU guides. This should be negligible.
2. **Measure directed scattering patterns** — the terminal node's scattering pattern IS the weight. Characterize it fully.
3. **Measure scattering efficiency** — what fraction of light is directed (computation) vs. absorbed or mode-mismatched (loss).
4. **Measure path integral fidelity** — compare the summed scattered fields at the output with the numerical reference.
5. **Do not measure "insertion loss"** — directed scattering is the computation, not a loss mechanism. Measure absorption and undesired scattering separately.
