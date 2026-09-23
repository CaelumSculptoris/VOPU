# Project Charter

## 1. Purpose

VOPU investigates whether three-dimensional refractive-index programming by
Implosion Carving can encode transformer weights in a monolithic optical
substrate with bound waveguides, fabricated linear transformations, and
localized passive nonlinear dynamics.

## 2. Primary research question

Can a monolithic 3D photonic volume implement a useful, measurable inference
primitive by physically encoding model weights in its geometry, refractive-index
landscape, terminal nodes, and passive material states?

## 3. Sub-questions

- Can post-shrinkage waveguides remain single-mode and low-loss over useful lengths?
- Can a compiler map transformer state dictionaries into a realizable 3D
  topology and compensate for shrinkage?
- Can terminal nodes realize calibrated complex scattering matrices and linear
  GEMM zones?
- Can phase and amplitude be preserved through a multi-node 3D network?
- Do RSA thresholding, excited-state lifetime, and Q/K XPM regions provide
  repeatable and sufficiently strong state-adaptive responses?
- What depth is possible before insertion loss and phase noise make computation unusable?
- Which fabrication throughput and yield are required for a credible cost model?

## 4. Scope

### In scope

- Optical routing, interference, and terminal-node linear transformations.
- Weight compilation, inverse-shrinkage compensation, and 3D topology synthesis.
- Material and geometry requirements for RSA, lifetime, and Kerr/XPM behavior.
- FDTD and reduced-order modeling.
- Small demonstrators and measurement protocols.
- Yield, packaging, and cost sensitivity.

### Out of scope for the first phase

- A complete transformer accelerator.
- Claims of general-purpose optical computing.
- Unverified commercial cost or energy claims.
- Human-subject, biomedical, or deployment applications.

## 5. Success criteria

The project passes its first feasibility gate when it has:

1. A measured or independently validated single-mode 3D routing path.
2. A compiler prototype that maps a defined weight tensor into a 3D design and
   records shrinkage compensation.
3. A calibrated terminal node with a repeatable complex transfer response.
4. A measured loss and phase-error budget across a multi-node path.
5. A validated nonlinear test fixture, even if the measured effect is
   insufficient for full inference.
6. A reproducible model whose predictions agree with measured linear behavior
   within a predefined tolerance.

## 6. Evidence labels

- **D — Demonstrated:** directly measured or reproduced from a cited source.
- **S — Simulated:** supported by a documented model and parameter set.
- **E — Estimated:** first-order calculation or engineering estimate.
- **H — Hypothesis:** plausible but not yet validated.

Every important result should carry one of these labels.

## 7. Non-goals and safeguards

The project must not describe an architectural possibility as an experimental result. Any use of intense laser power, nanomaterials, dopants, or supercritical fluids requires an appropriate institutional safety review before laboratory work.
