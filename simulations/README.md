# Simulation Work

Simulation work should progress from validated linear models to coupled nonlinear models.

## Recommended sequence

1. Scalar and vector mode analysis for post-shrinkage guide geometries.
2. Channel transparency characterization — propagation is fiber-like (negligible loss). Do not treat propagation as a primary loss term.
3. Terminal-node directed scattering simulation — model the scattering pattern, scattering efficiency (directed vs. absorbed/mismatched fraction), and complex transfer function.
4. Multi-node path integral accumulation with phase error propagation — the binding constraint is phase precision, not loss.
5. RSA two-level rate-equation model coupled to optical propagation (transparent below threshold).
6. Lifetime response and pulse-sequence simulations.
7. Kerr/XPM phase-shift model and comparison with full-wave results.
8. End-to-end path integral inference primitive with detector noise and calibration error.

## Baseline inputs

Use the Appendix A values from the source paper only as labeled baseline assumptions. Keep a separate file for measured updates, and never overwrite the baseline without recording a decision-log entry.

## Key modeling principles

1. **Directed scattering is computation, not loss.** Do not model node scattering as "insertion loss." The scattered field is the computational output. Only model absorbed or mode-mismatched light as loss.
2. **Propagation is fiber-optic.** Waveguide channels in a transparent medium have negligible propagation loss (~0.011 dB/cm including roughness). Do not treat propagation as a dominant loss term.
3. **Path integral summation is the accumulation mechanism.** The output is the coherent sum of all directed scattered fields. Model the interference, not just power transmission.
4. **Phase precision is the binding constraint.** Fabrication tolerance (±12 nm) introduces per-node phase uncertainty that accumulates as √N. This limits cascade depth, not loss.
5. **RSA zones are transparent below threshold.** Do not model RSA zones as lossy elements when below threshold.

## Required outputs

Each simulation run should produce configuration metadata, convergence evidence, parameter ranges, raw output, and a short interpretation stating whether the result is a demonstration, simulation, estimate, or hypothesis.
