# Models

Keep reduced-order and full-wave model definitions separate from generated outputs.

## Model layers

1. **Geometry layer:** written geometry, shrinkage map, and tolerances.
2. **Material layer:** index, absorption, lifetime, Kerr, and RSA parameters.
3. **Device layer:** mode propagation, node scattering, and nonlinear response.
4. **Network layer:** transfer matrices, loss, noise, and calibration.
5. **Application layer:** inference primitive and numerical reference.

Each model must declare its assumptions, parameter provenance, valid operating range, and known omissions.
