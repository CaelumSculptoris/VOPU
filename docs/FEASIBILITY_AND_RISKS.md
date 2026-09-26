# Feasibility, Claims, and Risks

## Claim register

| Claim | Type | Evidence needed | Status |
|---|---|---|---|
| Transformer weights can be compiled into a 3D optical topology with directed scattering nodes implementing each weight | H/S | Compiler prototype, scattering simulation, and design-to-measurement comparison | Open |
| ImpCarv can create sub-100 nm post-shrinkage features | D | Yang et al., *Nature Photonics* (2026), reporting 67 ± 12 nm lateral and 22 ± 2 nm axial features; independent reproduction and VOPU-specific transfer remain open | Source demonstrated; reproduction open |
| Waveguide channels in transparent medium have fiber-like (negligible) propagation loss | D/S | Fiber-optic principle: commercial PMMA fiber achieves 0.001 dB/cm at 520nm; ImpCarv hydrogel is transparent at 532nm; surface roughness adds ~0.01 dB/cm scattering | Principle established; VOPU-specific measurement open |
| Terminal nodes can produce directed scattering patterns implementing useful complex weights | H | Scattering pattern measurement, scattering efficiency characterization, and path integral comparison with numerical reference | Open |
| Path integral summation of scattered fields produces a measurable inference result | H | Output field measurement vs. numerical reference for a compiled weight tensor | Open |
| RSA can provide passive epsilon-thresholding (transparent below threshold) | H | Transmission, hysteresis, recovery, and damage tests | Open |
| Excited-state relaxation can provide useful lambda-decay temporal context | H | Pump-probe or pulse-response measurement | Open |
| Q/K XPM can produce a detectable dynamic operand interaction | H | Heterodyne phase measurement versus power, overlap, and pulse timing | Open |
| Phase relationships can be controlled with sufficient precision for multi-node path integral computation | E | Phase error budget, fabrication precision measurement, and calibration demonstration | Open |
| Unit cost can approach the paper's production targets | E | Measured throughput, yield, packaging, and capital model | Open |

## Highest risks

### R1 — Scattering pattern fidelity

Terminal nodes may not produce directed scattering patterns with sufficient precision or efficiency to implement useful weights. Undesired scattering into wrong modes would degrade the path integral.

**Mitigation:** characterize node scattering patterns independently before integration; measure scattering efficiency (directed fraction vs. absorbed/mismatched fraction); validate path integral summation against numerical reference at each depth.

### R2 — Phase precision in the path integral

The path integral summation depends on phase relationships between scattered fields. Fabrication tolerance (±12 nm) introduces per-node phase uncertainty that accumulates as √N. This is the binding constraint on cascade depth, not loss.

**Mitigation:** measure fabrication precision for VOPU-specific geometries; implement per-node phase calibration; maintain a phase error budget. Baseline simulation shows ~7 nodes at 45° tolerance, ~10 nodes at 90% fidelity.

### R3 — Nonlinear response too weak or too slow

The required XPM or RSA response may demand powers, interaction lengths, or recovery times incompatible with the intended system. XPM is the weakest link — pure PMMA Kerr is too weak; doped polymer or nanoparticle enhancement is needed.

**Mitigation:** characterize mechanisms in standalone test structures before integrating them. RSA is feasible (~17 mW threshold for PbPc at 532 nm). XPM requires material characterization of doped polymer or nanoparticle-enhanced hydrogel.

### R4 — Compiler-to-fabrication mismatch

Inverse shrinkage, material loading, and node placement may change the physical scattering pattern enough to invalidate the compiled operation.

**Mitigation:** preserve a design-to-fabrication trace, measure post-shrinkage geometry, and close the loop with calibrated scattering pattern reconstruction.

### R5 — Shrinkage distortion

Isotropic shrinkage may not remain sufficiently uniform around long, dense, or doped structures.

**Mitigation:** measure dimensional metrology at multiple locations and include deformation in inverse design.

### R6 — Defect sensitivity

A localized defect can disrupt a 3D channel or phase relationship across many downstream nodes.

**Mitigation:** define defect classes, inspect statistically, and report yield by functional primitive rather than only by sample.

### R7 — Calibration and packaging

The optical core may work while coupling, alignment, and thermal drift dominate system error. Coupling loss (input/output facets) is the largest single loss term in the system.

**Mitigation:** treat packaging as a first-class experiment with alignment tolerances, mode matching, and environmental perturbations.

### R8 — Cost-model optimism

The nominal materials floor excludes the dominant tool, labor, packaging, and yield terms.

**Mitigation:** update the model only from measured process time and compound yield.

## Go/no-go rules

- **Proceed to deeper networks** only if the validated path integral summation matches the numerical reference within the current error budget with margin.
- **Proceed to integrated nonlinear tests** only if the standalone nonlinear response is repeatable and does not damage the guide.
- **Pause scale-up** if measured phase drift or scattering pattern variation invalidates the path integral by more than the predefined tolerance.
- **Do not publish a performance claim** without raw data, calibration details, and uncertainty.
