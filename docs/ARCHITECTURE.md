# VOPU Architecture

## Signal path

1. An external source encodes complex payloads as optical amplitude and phase.
2. Face-coupled ports inject fields into a 3D single-mode waveguide graph.
3. Waveguides route fields along non-intersecting paths.
4. Terminal nodes apply calibrated complex scattering and interference.
5. Local nonlinear regions apply thresholding, temporal state, or field-field phase interaction.
6. Output fields are detected by homodyne or direct detection.
7. Calibration software reconstructs the intended linear or nonlinear operation.

## Functional blocks

| Block | Intended function | Primary measurement |
|---|---|---|
| Input coupler | Efficient field injection | Coupling efficiency and phase stability |
| 3D waveguide | Bound single-mode transport | Mode content, loss, crosstalk |
| Terminal node | Static complex weighting | Scattering matrix and repeatability |
| RSA zone | Intensity thresholding | Transmission versus intensity and recovery |
| Lifetime zone | Short-term memory | Impulse response and decay constant |
| XPM zone | Field-field interaction | Differential phase versus powers |
| Output detector | Field recovery | SNR, dynamic range, reconstruction error |

## Reference parameters

The source paper lists a 532 nm baseline wavelength, substrate index 1.48, peak index contrast 0.40, 0.25 dB/cm waveguide attenuation, 0.08 dB/node insertion loss, and a 1.2 ns nominal relaxation lifetime. These are starting parameters, not accepted specifications; provenance and measurement status must be recorded in the claim register.

## Critical interfaces

- Geometry-to-optical transfer: shrinkage must map written geometry to the intended post-shrinkage structure.
- Material-to-response transfer: dopant concentration and local chemistry must map to measured absorption, lifetime, and nonlinear coefficients.
- Optical-to-computation transfer: calibration must map measured complex fields to numerical tensor operations.
- Fabrication-to-economics transfer: yield and write throughput must be measured rather than inferred from idealized process conditions.
