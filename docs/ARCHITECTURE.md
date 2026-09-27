# VOPU Architecture

## Computational model

VOPU computes through directed scattering and path integral summation. Terminal nodes scatter light in directed patterns that implement weights. The scattered fields from all nodes sum via optical interference at the output. The interference pattern IS the inferred result. This is not a lossy photonic circuit — it is a volumetric optical computer where propagation, scattering, and interference are the computation.

## Signal path

1. A compiler extracts transformer state-dictionary weights and maps them to a 3D waveguide topology, terminal-node coordinates, and material assignments.
2. The compiler applies the inverse shrinkage deformation tensor so the post-ImpCarv geometry realizes the intended design.
3. An external SLM or laser interferometer encodes payloads as optical amplitude and phase.
4. Face-coupled ports inject fields into a monolithic 3D single-mode optical bus.
5. Waveguide channels route fields to terminal nodes. These channels are fiber-optic paths in a transparent medium — propagation loss is negligible.
6. Terminal nodes scatter the incoming fields in directed patterns that implement compiled weights. The directed scattering IS the computation. Only absorbed or mode-mismatched light is lost.
7. Scattered fields from all nodes propagate and sum via path integral at the output. The interference pattern IS the inferred result.
8. Passive nonlinear zones modulate the scattered fields: epsilon-thresholding (RSA), relaxation-based temporal context (lambda-decay), and Q/K cross-phase interaction (XPM).
9. Output fields are detected by homodyne or direct detection.
10. Calibration software reconstructs the transformed fields and compares them with the numerical reference.

## Functional blocks

| Block | Intended function | Primary measurement |
|---|---|---|
| Input coupler | Efficient field injection | Coupling efficiency and phase stability |
| 3D waveguide | Bound single-mode transport (fiber-like) | Mode content, scattering efficiency, transparency |
| Terminal node | Directed scattering implementing weights | Scattering pattern, scattering efficiency, repeatability |
| RSA zone | Intensity thresholding (transparent below threshold) | Transmission versus intensity and recovery |
| Lifetime zone | Short-term memory | Impulse response and decay constant |
| XPM zone | Dynamic Q/K interaction | Differential phase versus powers and overlap |
| Output detector | Path integral field recovery | SNR, dynamic range, reconstruction error |

## Weight and state mapping

### Frozen volumetric weights

The trained transformer state dictionary is compiled into a permanent physical configuration. Weight tensors are represented by combinations of:

- waveguide topology and path selection;
- refractive-index landscape and local index contrast;
- terminal-node directed scattering patterns;
- phase shifts and coupling strengths; and
- node geometry and incidence/coupling angle.

The resulting crystal is a static physical weight store. Runtime computation occurs as directed scattering and path integral summation of optical fields through the compiled network.

### Passive state adaptivity

The static weight configuration is supplemented by material state:

- **Epsilon-thresholding:** reverse-saturable-absorber zones are transparent below threshold and absorb above it, suppressing sub-threshold activations and transmitting sufficiently strong fields.
- **Lambda-decay:** excited chromophore states temporarily change refractive index and absorption, then relax with characteristic lifetime `tau`, giving sequential pulses temporal context.
- **Dynamic Q/K interaction:** overlapping query and key fields modulate refractive paths through cross-phase modulation, supplying a physical operand interaction.

These mechanisms are proposed device functions and require independent characterization before system-level claims.

## Compiler and fabrication workflow

1. Extract `Wq`, `Wk`, `Wv`, and feed-forward weights.
2. Synthesize the 3D interconnect topology and terminal-node locations.
3. Apply inverse shrinkage compensation.
4. Prepare the doped hydrogel precursor.
5. Two-photon scribe channels and node coordinates.
6. Apply ionic dehydration and supercritical CO2 drying.
7. Package the crystal in an aligned optical housing.
8. Launch encoded fields and compare homodyne readout with the compiled numerical reference.

## Reference parameters

The source architecture uses a 532 nm baseline wavelength, approximately 1.48 substrate index, approximately 0.40 peak index contrast, and a 1.2 ns nominal relaxation lifetime. Propagation loss through waveguide channels is fiber-like (negligible) — these are transparent channels in a transparent medium, not lossy interconnects. The only node-related loss is material absorption (a small fraction of the directed field); directed scattering is the computational operation, not a loss source. RSA zones below threshold are transparent. These are starting parameters, not accepted specifications; provenance and measurement status must be recorded in the claim register.

## Critical interfaces

- Geometry-to-scattering transfer: shrinkage must map written geometry to the intended post-shrinkage scattering pattern.
- Material-to-response transfer: dopant concentration and local chemistry must map to measured absorption, lifetime, and nonlinear coefficients.
- Scattering-to-computation transfer: calibration must map measured scattered fields to numerical tensor operations via path integral reconstruction.
- Compiler-to-geometry transfer: the inverse-shrinkage-compensated design must survive fabrication without changing the compiled operation.
- Fabrication-to-economics transfer: yield and write throughput must be measured rather than inferred from idealized process conditions.
