# Experiment Matrix

| ID | Experiment | Independent variable | Measurements | Control | Exit criterion |
|---|---|---|---|---|---|
| E01 | Straight-guide transparency | Length, geometry, wavelength | Transmission, mode profile, phase, propagation loss | Unpatterned reference | Fiber-like transparency with negligible propagation loss |
| E02 | Bend and crossing tolerance | Bend radius, separation | Crosstalk, radiation loss, mode purity | Straight guide | Tolerance map suitable for topology synthesis |
| E03 | Terminal-node directed scattering | Node geometry/material | Scattering pattern, scattering efficiency (directed vs. absorbed/mismatched), complex transfer function | Empty node / reference path | Calibrated repeatable directed scattering pattern with measured efficiency |
| E04 | Multi-node path integral | Node count and spacing | Output field vs. numerical reference, phase error, path integral fidelity | Numerical simulation | Measured path integral matches reference within tolerance |
| E05 | RSA threshold | Input intensity and pulse width | Transmission, recovery, hysteresis (transparent below threshold) | Passive host material | Stable threshold with quantified drift |
| E06 | Lifetime memory | Pulse spacing and wavelength | Transient index/absorption response | Untreated host | Decay fit and usable operating window |
| E07 | XPM phase shift | Pump/probe power and overlap | Differential phase | Probe-only and pump-only | Phase shift above measurement noise without damage |
| E08 | Packaging/alignment | Lateral, angular, thermal offsets | Coupling loss and output error | Nominal alignment | Alignment tolerance budget |
| E09 | Inference primitive | Input vector and programmed weights | Optical output (path integral) versus reference | Numerical model | Predefined error and repeatability threshold |
| E10 | Process yield | Batch and process condition | Defect class, functional pass rate | Process-control sample | Yield estimate with confidence interval |

## Required record for every experiment

- Date, operator, sample identifier, and instrument identifiers.
- Geometry/design revision and material batch.
- Raw data location and checksum.
- Calibration procedure and reference standard.
- Environmental conditions.
- Predefined acceptance criterion.
- Deviations, failed trials, and analysis version.
