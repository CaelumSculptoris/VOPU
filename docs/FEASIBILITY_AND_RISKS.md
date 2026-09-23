# Feasibility, Claims, and Risks

## Claim register

| Claim | Type | Evidence needed | Status |
|---|---|---|---|
| ImpCarv can create sub-100 nm post-shrinkage features | D | Yang et al., *Nature Photonics* (2026), reporting 67 ± 12 nm lateral and 22 ± 2 nm axial features; independent reproduction and VOPU-specific transfer remain open | Source demonstrated; reproduction open |
| 3D channels can remain single-mode after shrinkage | H | Mode simulation plus near/far-field measurement | Open |
| Terminal nodes can realize useful complex weights | H | Transfer-matrix calibration across devices | Open |
| RSA can provide a stable optical threshold | H | Transmission, hysteresis, recovery, and damage tests | Open |
| Lifetime engineering can provide useful temporal memory | H | Pump-probe or pulse-response measurement | Open |
| XPM can produce a detectable product-scale phase shift | H | Heterodyne phase measurement versus power and overlap | Open |
| A single transit can support useful depth | E | Loss, noise, phase, and crosstalk budget | Open |
| Unit cost can approach the paper's production targets | E | Measured throughput, yield, packaging, and capital model | Open |

## Highest risks

### R1 — Cascadability failure

Loss and phase error may compound too quickly for a useful network.

**Mitigation:** measure each primitive separately; maintain a pessimistic budget including coupling, node, propagation, detector, and calibration losses.

### R2 — Nonlinear response too weak or too slow

The required XPM or RSA response may demand powers, interaction lengths, or recovery times incompatible with the intended system.

**Mitigation:** characterize mechanisms in standalone test structures before integrating them.

### R3 — Shrinkage distortion

Isotropic shrinkage may not remain sufficiently uniform around long, dense, or doped structures.

**Mitigation:** measure dimensional metrology at multiple locations and include deformation in inverse design.

### R4 — Defect sensitivity

A localized defect can disrupt a 3D channel or phase relationship across many downstream nodes.

**Mitigation:** define defect classes, inspect statistically, and report yield by functional primitive rather than only by sample.

### R5 — Calibration and packaging

The optical core may work while coupling, alignment, and thermal drift dominate system error.

**Mitigation:** treat packaging as a first-class experiment with alignment tolerances and environmental perturbations.

### R6 — Cost-model optimism

The nominal materials floor excludes the dominant tool, labor, packaging, and yield terms.

**Mitigation:** update the model only from measured process time and compound yield.

## Go/no-go rules

- **Proceed to deeper networks** only if the validated linear primitive meets the current error budget with margin.
- **Proceed to integrated nonlinear tests** only if the standalone nonlinear response is repeatable and does not damage the guide.
- **Pause scale-up** if measured phase drift or loss invalidates the depth model by more than the predefined tolerance.
- **Do not publish a performance claim** without raw data, calibration details, and uncertainty.
