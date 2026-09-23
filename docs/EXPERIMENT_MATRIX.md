# Experiment Matrix

| ID | Experiment | Independent variable | Measurements | Control | Exit criterion |
|---|---|---|---|---|---|
| E01 | Straight-guide routing | Length, geometry, wavelength | Insertion loss, mode profile, phase | Unpatterned reference | Single-mode behavior and repeatable loss |
| E02 | Bend and crossing tolerance | Bend radius, separation | Crosstalk, excess loss | Straight guide | Tolerance map suitable for topology synthesis |
| E03 | Terminal-node response | Node geometry/material | Complex scattering matrix | Empty node / reference path | Calibrated repeatable transfer matrix |
| E04 | Multi-node cascade | Node count and spacing | OSNR, phase error, total loss | Numerical cascade | Measured depth trend agrees with model |
| E05 | RSA threshold | Input intensity and pulse width | Transmission, recovery, hysteresis | Passive host material | Stable threshold with quantified drift |
| E06 | Lifetime memory | Pulse spacing and wavelength | Transient index/absorption response | Untreated host | Decay fit and usable operating window |
| E07 | XPM phase shift | Pump/probe power and overlap | Differential phase | Probe-only and pump-only | Phase shift above measurement noise without damage |
| E08 | Packaging/alignment | Lateral, angular, thermal offsets | Coupling loss and output error | Nominal alignment | Alignment tolerance budget |
| E09 | Inference primitive | Input vector and programmed weights | Optical output versus reference | Numerical model | Predefined error and repeatability threshold |
| E10 | Process yield | Batch and process condition | Defect class, functional pass rate | Process-control sample | Yield estimate with confidence interval |

## Required record for every experiment

- Date, operator, sample identifier, and instrument identifiers.
- Geometry/design revision and material batch.
- Raw data location and checksum.
- Calibration procedure and reference standard.
- Environmental conditions.
- Predefined acceptance criterion.
- Deviations, failed trials, and analysis version.
