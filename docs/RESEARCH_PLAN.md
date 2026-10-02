# Research Plan

## Work packages

### WP1 — Claim and literature validation

Extract every quantitative claim from the source papers and architectural specification, identify its provenance, and classify it as D/S/E/H. Verify the ImpCarv fabrication basis, compiler assumptions, and all cited material parameters.

**Deliverables:** claim register, annotated bibliography, parameter provenance table.

### WP2 — Directed scattering primitive

Model and test a short hollow-core 3D path defined by elongated ImpCarv cavities. Track the cavity from liquid-filled post-exposure state through washing, solvent exchange, ionic shrinkage, and supercritical drying; then characterize its final mode and loss. Separately test dopant-mediated reflective-node conversion, reflectance, angular scattering, and phase stability.

**Deliverables:** baseline model, test fixture, scattering pattern measurements, scattering efficiency characterization.

### WP3 — Volumetric path integral scaling

Extend WP2 to multiple nodes and non-intersecting paths. Determine how phase error, scattering pattern variation, and path integral fidelity accumulate with depth. Validate that the summed scattered fields match the numerical reference.

**Deliverables:** depth-vs-fidelity curves and a validated cascability budget based on measured propagation, mode, scattering, and phase errors.

### WP4 — Nonlinear and temporal materials

Characterize RSA thresholding (transparent below threshold), excited-state recovery, and Q/K cross-phase interaction independently before combining them with the linear network.

**Deliverables:** intensity-response curves, recovery curves, phase-shift measurements, damage and drift limits.

### WP5 — Weight compiler and geometry realization

Build the latent-graph compiler that extracts `Wq`, `Wk`, `Wv`, and feed-forward weights; synthesizes a 3D topology and terminal-node map; applies inverse shrinkage compensation; and emits fabrication and calibration artifacts.

**Deliverables:** compiler specification, test vectors, topology files, shrinkage-compensation report, and design-to-measurement traceability.

### WP6 — System-level inference primitive

Implement the compiler and one narrow, measurable operation such as a calibrated matrix-vector product or thresholded classifier. Specify a prompt preprocessing step that produces the operation's numerical input, map it to a calibrated coherent optical field, measure and reconstruct the output, then decode it for the bounded task. Compare the complete digital/optical path with a numerical reference; do not equate this milestone with a complete language model.

**Deliverables:** task and prompt preprocessing definition, optical encoder calibration, detector/readout and decoder, dataset, end-to-end error analysis, repeatability report.

### WP7 — Manufacturing and economics

Replace nominal cost assumptions with measured write time, precursor usage, packaging time, yield, and failure modes.

**Deliverables:** parameterized cost model and sensitivity report.

## Milestones

| ID | Milestone | Exit condition |
|---|---|---|
| M0 | Research baseline | Charter, claim register, and reproducibility conventions complete |
| M1 | Cavity channel validated | Verified post-process gas-filled lumen with a measured guided mode, loss, and phase behavior meeting pre-registered criteria |
| M2 | Reflective node validated | Dopant-mediated metal feature and directed angular response are repeatable and calibrated |
| M3 | Path integral validated | Multi-node summed scattered fields match numerical reference within tolerance |
| M4 | Nonlinearity characterized | At least one nonlinear mechanism has a quantified usable range |
| M5 | Primitive demonstrated | End-to-end optical operation beats a defined error threshold |
| M6 | Scale decision | Evidence supports scale-up, redesign, or stop |

## Dependencies

WP2 depends on WP1. WP3 depends on WP2. WP4 depends on WP1 and can proceed in parallel with WP2. WP5 depends on WP1 and WP3. WP6 depends on WP4 and WP5 as well as the validated linear path. WP7 can begin with estimates but requires WP2, WP3, and WP6 data for a credible update.
