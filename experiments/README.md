# Experimental Work

This folder contains protocols, sample records, measurement plans, and bench notes. Start with the experiments in [`../docs/EXPERIMENT_MATRIX.md`](../docs/EXPERIMENT_MATRIX.md).

## First protocol package

- E01: straight hollow-core ImpCarv channel guidance, including wash/dry-state verification, post-shrink cross-section, lumen-mode confinement, and cutback-loss measurements.
- E02: bend, spacing, and crosstalk tolerance.
- E03: terminal-node directed scattering pattern and efficiency calibration.
- E08: coupling and alignment tolerance.
- E09: prompt-derived feature encoding through optical readout and digital decoding for a bounded inference task, after the linear path and calibration pass.

Nonlinear tests should begin only after the linear reference paths and measurement calibration are stable. Any work involving lasers, dopants, nanoparticles, solvents, or supercritical CO2 requires appropriate safety procedures and facility approval.

## Key experimental principles

1. **Measure guided-channel performance** — verify liquid removal and open-lumen survival, then measure the final cavity/gel boundary, mode confinement, propagation loss, and phase stability; do not presume negligible loss.
2. **Measure directed scattering patterns** — the terminal node's scattering pattern IS the weight. Characterize it fully.
3. **Measure scattering efficiency** — what fraction of light is directed (computation) vs. absorbed or mode-mismatched (loss).
4. **Measure path integral fidelity** — compare the summed scattered fields at the output with the numerical reference.
5. **Decompose node transfer.** Measure intended directed output, absorption, and parasitic scattering/mode mismatch separately; report total transfer where it helps characterize the device.
