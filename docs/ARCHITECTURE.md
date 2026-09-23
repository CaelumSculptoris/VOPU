# VOPU Architecture

## Signal path

1. A compiler extracts transformer state-dictionary weights and maps them to a
   3D waveguide topology, terminal-node coordinates, and material assignments.
2. The compiler applies the inverse shrinkage deformation tensor so the
   post-ImpCarv geometry realizes the intended design.
3. An external SLM or laser interferometer encodes payloads as optical
   amplitude and phase.
4. Face-coupled ports inject fields into a monolithic 3D single-mode optical
   bus.
5. Non-intersecting waveguides route fields deterministically to terminal nodes.
6. Terminal nodes apply static scattering, reflection, phase shifts, and
   interference that implement compiled linear operations.
7. Passive nonlinear zones apply epsilon-thresholding, relaxation-based
   temporal context, and Q/K cross-phase interaction.
8. Output fields are detected by homodyne or direct detection.
9. Calibration software reconstructs the transformed fields and compares them
   with the numerical reference.

## Functional blocks

| Block | Intended function | Primary measurement |
|---|---|---|
| Input coupler | Efficient field injection | Coupling efficiency and phase stability |
| 3D waveguide | Bound single-mode transport | Mode content, loss, crosstalk |
| Terminal node | Static complex weighting | Scattering matrix and repeatability |
| RSA zone | Intensity thresholding | Transmission versus intensity and recovery |
| Lifetime zone | Short-term memory | Impulse response and decay constant |
| XPM zone | Dynamic Q/K interaction | Differential phase versus powers and overlap |
| Output detector | Field recovery | SNR, dynamic range, reconstruction error |

## Weight and state mapping

### Frozen volumetric weights

The trained transformer state dictionary is compiled into a permanent physical
configuration. Weight tensors are represented by combinations of:

- waveguide topology and path selection;
- refractive-index landscape and local index contrast;
- terminal-node scattering and reflection;
- phase shifts and coupling strengths; and
- node geometry and incidence/coupling angle.

The resulting crystal is a static physical weight store. Runtime computation
occurs as phase- and amplitude-encoded fields propagate through the compiled
network.

### Passive state adaptivity

The static weight configuration is supplemented by material state:

- **Epsilon-thresholding:** reverse-saturable-absorber zones suppress
  sub-threshold activations and transmit sufficiently strong fields.
- **Lambda-decay:** excited chromophore states temporarily change refractive
  index and absorption, then relax with characteristic lifetime `tau`, giving
  sequential pulses temporal context.
- **Dynamic Q/K interaction:** overlapping query and key fields modulate
  refractive paths through cross-phase modulation, supplying a physical
  operand interaction.

These mechanisms are proposed device functions and require independent
characterization before system-level claims.

## Compiler and fabrication workflow

1. Extract `Wq`, `Wk`, `Wv`, and feed-forward weights.
2. Synthesize the 3D interconnect topology and terminal-node locations.
3. Apply inverse shrinkage compensation.
4. Prepare the doped hydrogel precursor.
5. Two-photon scribe channels and node coordinates.
6. Apply ionic dehydration and supercritical CO2 drying.
7. Package the crystal in an aligned optical housing.
8. Launch encoded fields and compare homodyne readout with the compiled
   numerical reference.

## Reference parameters

The source architecture uses a 532 nm baseline wavelength, approximately
1.48 substrate index, approximately 0.40 peak index contrast, 0.25 dB/cm
waveguide attenuation, 0.08 dB/node insertion loss, and a 1.2 ns nominal
relaxation lifetime. These are starting parameters, not accepted
specifications; provenance and measurement status must be recorded in the
claim register.

## Critical interfaces

- Geometry-to-optical transfer: shrinkage must map written geometry to the intended post-shrinkage structure.
- Material-to-response transfer: dopant concentration and local chemistry must map to measured absorption, lifetime, and nonlinear coefficients.
- Optical-to-computation transfer: calibration must map measured complex fields to numerical tensor operations.
- Compiler-to-geometry transfer: the inverse-shrinkage-compensated design must survive fabrication without changing the compiled operation.
- Fabrication-to-economics transfer: yield and write throughput must be measured rather than inferred from idealized process conditions.
