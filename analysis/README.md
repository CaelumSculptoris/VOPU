# Analysis Work

Analysis converts raw measurements and simulation outputs into calibrated metrics and reports.

## Core metrics

- Channel performance: post-shrink propagation loss per centimeter, mode confinement, and phase stability (measured; no negligible-loss assumption).
- Mode purity and crosstalk.
- Scattering efficiency: fraction of field directed to target vs. absorbed or mode-mismatched.
- Directed scattering pattern: complex transfer function and repeatability.
- Path integral fidelity: output field vs. numerical reference.
- Phase error accumulation: per-node uncertainty and depth scaling.
- Coupling efficiency at input/output facets (largest single loss term).
- Prompt-feature encoder error and repeatability; optical field-to-feature reconstruction error.
- End-to-end bounded-task error, including prompt preprocessing and digital decoding against a numerical reference.
- OSNR and detector dynamic range.
- Phase drift versus time, temperature, and alignment.
- RSA threshold, extinction ratio, recovery time, and hysteresis (transparent below threshold).
- XPM phase shift per power and interaction length.
- Functional yield and confidence interval.
- End-to-end optical-operation error against a numerical reference.

Every analysis should state the reference, units, uncertainty method, replicate count, and acceptance threshold.
