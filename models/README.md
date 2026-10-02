# Models

Keep reduced-order and full-wave model definitions separate from generated outputs.

## Model layers

1. **Geometry layer:** written geometry, cavity connectivity and process-stage contents, shrinkage map, and tolerances.
2. **Material layer:** index, absorption, lifetime, Kerr, and RSA parameters.
3. **Device layer:** mode propagation, directed scattering patterns, and nonlinear response.
4. **Network layer:** path integral summation, phase accumulation, coupling, and calibration.
5. **Interface layer:** prompt preprocessing, numerical-to-optical encoding, detector/readout, and digital decoding.
6. **Application layer:** bounded inference primitive and end-to-end numerical reference.

## Modeling principles

1. **Directed scattering is the proposed computation primitive.** Model terminal nodes as scattering elements with measured complex transfer functions. Count intended directed output as computation and absorbed or mismatched light as loss.
2. **Propagation is structure-specific.** Model the hollow lumen and its antiresonant/photonic-bandgap boundary, then use measured or swept confinement and loss. Do not apply a solid-core step-index model or use the unsupported ~0.011 dB/cm estimate as a default.
3. **Path integral is the accumulation.** The output is the coherent sum of all directed scattered fields. Model the interference pattern, not just power transmission.
4. **Separate optical computation from prompt processing.** Explicitly model numerical feature inputs, optical amplitude/phase encoding, transfer, detection, and decoding. A field transformation alone does not implement a complete language model.
5. **Determine the binding constraint from data.** Model hollow-mode leakage, propagation, node scattering, fabrication tolerance, and phase drift; do not assume phase precision alone limits cascade depth.
6. **Treat nonlinear responses as hypotheses until measured.** Only use RSA, lifetime, or XPM terms when supported by characterized material parameters.

Each model must declare its assumptions, parameter provenance, valid operating range, and known omissions.
