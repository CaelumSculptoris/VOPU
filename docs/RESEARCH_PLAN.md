# Research Plan

## Work packages

### WP1 — Claim and literature validation

Extract every quantitative claim from the source paper, identify its provenance, and classify it as D/S/E/H. Verify the ImpCarv fabrication basis and all cited material parameters.

**Deliverables:** claim register, annotated bibliography, parameter provenance table.

### WP2 — Linear photonic primitive

Model and test a short 3D single-mode waveguide path, a splitter/combiner, and one terminal node. Establish mode quality, insertion loss, phase stability, and tolerance to geometry error.

**Deliverables:** baseline model, test fixture, transfer-matrix measurements.

### WP3 — Volumetric network scaling

Extend WP2 to multiple nodes and non-intersecting paths. Determine how loss, crosstalk, phase error, and fabrication defects accumulate with depth.

**Deliverables:** depth-vs-fidelity curves and a validated cascability budget.

### WP4 — Nonlinear and temporal materials

Characterize RSA thresholding, excited-state recovery, and XPM independently before combining them with the linear network.

**Deliverables:** intensity-response curves, recovery curves, phase-shift measurements, damage and drift limits.

### WP5 — System-level inference primitive

Implement one narrow, measurable operation such as a calibrated matrix-vector product, thresholded classifier, or low-dimensional QK/V interaction. Compare optical output with a numerical reference.

**Deliverables:** dataset, calibration procedure, error analysis, repeatability report.

### WP6 — Manufacturing and economics

Replace nominal cost assumptions with measured write time, precursor usage, packaging time, yield, and failure modes.

**Deliverables:** parameterized cost model and sensitivity report.

## Milestones

| ID | Milestone | Exit condition |
|---|---|---|
| M0 | Research baseline | Charter, claim register, and reproducibility conventions complete |
| M1 | Linear path validated | Single-mode routing and phase measurement are repeatable |
| M2 | Node validated | Terminal-node transfer matrix is calibrated |
| M3 | Cascability characterized | Multi-node loss/phase budget agrees with measurements |
| M4 | Nonlinearity characterized | At least one nonlinear mechanism has a quantified usable range |
| M5 | Primitive demonstrated | End-to-end optical operation beats a defined error threshold |
| M6 | Scale decision | Evidence supports scale-up, redesign, or stop |

## Dependencies

WP2 depends on WP1. WP3 depends on WP2. WP5 depends on WP3 and WP4. WP6 can begin with estimates but requires WP2/WP3 data for a credible update.
