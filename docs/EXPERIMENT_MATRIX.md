# Experiment Matrix

| ID | Experiment | Independent variable | Measurements | Control | Exit criterion |
|---|---|---|---|---|---|
| E01 | Hollow-core ImpCarv channel guidance | Wash/dry process, endpoint access, plain lumen versus structured cavity/web boundary, length, wavelength | Cavity contents by process stage, endpoint connectivity, post-shrink geometry, lumen mode profile, confinement/leakage, cutback loss, phase stability | Plain-lumen and non-guiding geometry controls | Verified liquid removal and final gas-filled open lumen with reproducible hollow-mode confinement and pre-registered loss criteria |
| E02 | Bend and crossing tolerance | Bend radius, separation | Crosstalk, radiation loss, mode purity | Passing straight guide | Tolerance map suitable for topology synthesis |
| E03 | Dopant-mediated reflective node | Dopant chemistry, exposure, facet geometry/orientation | Conversion/composition, facet morphology, wavelength-dependent reflectance/absorption, angular scattering, complex transfer function | Undoped gel and unexposed doped gel | Repeatable metal feature with calibrated reflectance and directed response |
| E04 | Multi-node path integral | Node count and spacing | Output field vs. numerical reference, phase error, path integral fidelity | Numerical simulation | Measured path integral matches reference within tolerance |
| E05 | RSA threshold | Input intensity and pulse width | Transmission, recovery, hysteresis (transparent below threshold) | Passive host material | Stable threshold with quantified drift |
| E06 | Lifetime memory | Pulse spacing and wavelength | Transient index/absorption response | Untreated host | Decay fit and usable operating window |
| E07 | XPM phase shift | Pump/probe power and overlap | Differential phase | Probe-only and pump-only | Phase shift above measurement noise without damage |
| E08 | Packaging/alignment | Lateral, angular, thermal offsets | Coupling loss and output error | Nominal alignment | Alignment tolerance budget |
| E09 | Prompt-to-optical inference interface | Prompt-derived feature vector, optical encoding, programmed weights, detector/decoder configuration | Encoding error, measured optical output, reconstructed numerical output, task result versus reference | Numerical pipeline with identical input and weights | End-to-end bounded-task error and repeatability thresholds met; all digital and optical stages documented |
| E10 | Process yield | Batch and process condition | Defect class, functional pass rate | Process-control sample | Yield estimate with confidence interval |

## Required record for every experiment

- Date, operator, sample identifier, and instrument identifiers.
- Geometry/design revision and material batch.
- Raw data location and checksum.
- Calibration procedure and reference standard.
- Environmental conditions.
- Predefined acceptance criterion.
- Deviations, failed trials, and analysis version.
