# Simulation Work

Simulation work should progress from validated linear models to coupled nonlinear models.

## Recommended sequence

1. Scalar and vector mode analysis for post-shrinkage guide geometries.
2. Straight-guide propagation loss and bend/crosstalk sweeps.
3. Terminal-node scattering and phase response.
4. Multi-node transfer-matrix cascade with uncertainty propagation.
5. RSA two-level rate-equation model coupled to optical propagation.
6. Lifetime response and pulse-sequence simulations.
7. Kerr/XPM phase-shift model and comparison with full-wave results.
8. End-to-end inference primitive with detector noise and calibration error.

## Baseline inputs

Use the Appendix A values from the source paper only as labeled baseline assumptions. Keep a separate file for measured updates, and never overwrite the baseline without recording a decision-log entry.

## Required outputs

Each simulation run should produce configuration metadata, convergence evidence, parameter ranges, raw output, and a short interpretation stating whether the result is a demonstration, simulation, estimate, or hypothesis.
