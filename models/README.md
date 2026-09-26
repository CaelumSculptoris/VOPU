# Models

Keep reduced-order and full-wave model definitions separate from generated outputs.

## Model layers

1. **Geometry layer:** written geometry, shrinkage map, and tolerances.
2. **Material layer:** index, absorption, lifetime, Kerr, and RSA parameters.
3. **Device layer:** mode propagation, directed scattering patterns, and nonlinear response.
4. **Network layer:** path integral summation, phase accumulation, coupling, and calibration.
5. **Application layer:** inference primitive and numerical reference.

## Modeling principles

1. **Directed scattering is computation.** Model terminal nodes as scattering elements that redirect light according to compiled weights. The scattered field is the computational output, not a loss term.
2. **Propagation is fiber-optic.** Model waveguide channels as fiber with negligible loss (~0.011 dB/cm including surface roughness).
3. **Path integral is the accumulation.** The output is the coherent sum of all directed scattered fields. Model the interference pattern, not just power transmission.
4. **Phase precision is the binding constraint.** Model fabrication tolerance as per-node phase uncertainty that accumulates as √N across the network.
5. **RSA zones are transparent below threshold.** Only model absorption when the field exceeds the RSA threshold.

Each model must declare its assumptions, parameter provenance, valid operating range, and known omissions.
