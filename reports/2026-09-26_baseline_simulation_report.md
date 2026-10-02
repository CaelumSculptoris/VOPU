# VOPU Baseline Simulation Report (Revised)

**Date:** 2026-09-26  
**Evidence level:** S (simulated) for all results; D (demonstrated) for literature-validated parameters  
**Author:** Perplexity Computer (automated analysis)

---

## Executive Summary

This report presents the first quantitative baseline physics analysis for the VOPU architecture, revised to reflect the correct computational model: VOPU computes through directed scattering and path integral summation, not through lossy photonic interconnects.

**Key finding (conditional model):** The report's 5-10 node estimates assume a hypothetical guided channel and assumed propagation loss. They do not establish a fabricated VOPU guide, negligible propagation loss, or that phase error rather than loss is the binding constraint. Terminal nodes are intended to compute through directed scattering, but desired output and parasitic scattering/absorption still require measurement.

**Go/No-Go recommendation:** Proceed to a straight-guide feasibility experiment first. The simulated network is a conditional design study, not demonstrated device feasibility.

## Evidence correction (2026-10-01)

The earlier "fiber-optic principle" discussion conflated the existence of guided-wave physics with the loss of an unbuilt VOPU channel. The selected VOPU path is an ImpCarv lumen that is liquid-filled during washing and intended to become gas-filled after solvent exchange, ionic shrinkage, and supercritical-CO2 drying. Verify removal of liquid/residue and survival of the lumen. Water-jet guiding does not establish confinement in this reversed final index ordering, and none of the solid-core parameters or the 0.011 dB/cm estimate below characterize an ImpCarv hollow-core guide. Treat all loss and cascade-depth results as conditional model outputs only. E01 must measure final lumen/boundary geometry, hollow-mode profile, cutback loss, and phase stability before those outputs can inform a go/no-go decision.

---

## 1. Mode Analysis [S] — Superseded for hollow-core channels

### Single-mode condition

| Parameter Set | n_core | n_clad | NA | Max single-mode diameter |
|---|---|---|---|---|
| VOPU REV8 spec | 1.88 | 1.48 | 1.159 | 351 nm |
| ImpCarv demonstrated | 1.5 | 1.0 | 1.118 | 364 nm |

These maximum diameters are idealized solid-core step-index model values and do not apply to the selected hollow-core antiresonant channel. ImpCarv's reported vacancy feature size does not demonstrate that a hollow-core boundary or guided mode can be fabricated.

---

## 2. Loss Budget — Corrected [S], not applicable to hollow-core ImpCarv channels

### Reference values and unvalidated model assumptions

The following values are comparison points or assumptions, not measured ImpCarv-guide performance:

| Channel type | Loss | Source |
|---|---|---|
| Silica fiber (1550 nm) | 0.000002 dB/cm | [D] telecom standard |
| PMMA plastic fiber (520 nm) | 0.001 dB/cm | [D] commercial POF |
| Assumed VOPU propagation input (532 nm) | 0.011 dB/cm | [E] unvalidated model assumption; not an ImpCarv measurement |
| REV8 spec placeholder | 0.25 dB/cm | [E] unvalidated model assumption |

### Illustrative loss breakdown at 10 nodes (conditional model)

| Loss source | Loss | Share | Note |
|---|---|---|---|
| Coupling (in/out) | 0.5 dB | 35% | Getting light into the volume |
| Node absorption | 0.88 dB | 62% | Only absorbed light — directed scattering is computation |
| Propagation | 0.01 dB | 0.8% | Follows from the assumed 0.011 dB/cm input; unmeasured. |
| Bends | 0.03 dB | 2% | Small |
| **Total** | **1.4 dB** | | SNR: 78.6 dB |
| Directed scattering | **N/A** | | IS the computation |

### Max cascade depth (loss-limited; superseded for the selected channel)

| Scenario | Max depth |
|---|---|
| Fiber-like propagation + node absorption | 706 nodes |
| Optimized nodes + mode-matched coupling | 1,929 nodes |
| Original spec placeholder (0.25 dB/cm) | 561 nodes |

These cascade-depth results are conditional on assumed solid-core channel and node losses; they do not show that the selected hollow-core channel permits 700+ nodes. The binding constraint is not established until hollow-channel confinement, propagation, and node losses are measured.

---

## 3. Phase Error Budget [S]

### Per-node phase error breakdown

| Error Source | Per-node σ (degrees) | Fraction of total |
|---|---|---|
| Fabrication tolerance (±12 nm) | 13.7° | 68% |
| Node scattering variation (±5%) | 9.0° | 29% |
| Index variation (±1% of Δn) | 1.4° | <1% |
| Thermal node drift (±0.5 K) | ~0° | <1% |
| **Total per-node** | **16.4°** | **100%** |

### Cascade depth limits (phase-based)

| Tolerance | Max depth |
|---|---|
| 45° (loose) | 7 nodes |
| 22.5° (strict) | 2 nodes |

**Fabrication tolerance is the binding constraint.** The ±12 nm ImpCarv precision translates to ~13.7° per-node phase uncertainty. This is the critical path to deeper networks.

---

## 4. Nonlinear Mechanism Estimates [S, with D literature parameters]

### RSA: Feasible

PbPc at 532 nm: threshold ~17 mW guided power, ~18 dB extinction ratio. RSA zones are transparent below threshold.

### Lifetime: Plausible

VOPU's 1.2 ns reference is shorter than ZnPc S1 (2.88 ns) but reasonable for doped hydrogel.

### XPM: Requires material engineering

Pure PMMA Kerr needs 13 W for 45° phase shift. Doped polymer (n2 ~ 10⁻¹⁶) needs 131 mW — challenging but possible. Thermal hydrogel nonlinearity is strong but too slow.

---

## 5. Cascability [S]

| Fidelity threshold | Max depth |
|---|---|
| 90% fidelity | 10 nodes |
| 50% fidelity | 30 nodes |

The report's assumed-input model identifies phase as its binding constraint, but this is conditional: measured channel loss and phase behavior could change the result.

---

## 6. Weight Compiler Prototype [S]

A working compiler prototype maps weight matrices to 3D terminal-node topology with inverse shrinkage compensation (5.03× MSF factor) and numerical reference generation.

---

## 7. Recommendations

1. Fabricate and measure a straight hollow-core ImpCarv channel (E01), including post-shrink lumen/boundary geometry, hollow-mode confinement, cutback loss, and phase stability
2. Calibrate one terminal node (E03) to establish directed scattering pattern and efficiency
3. Measure actual ImpCarv dimensional tolerance for VOPU-specific geometries
4. Implement per-node phase calibration to compensate fabrication errors
5. Characterize PbPc-doped hydrogel RSA response at 532 nm in solid state
6. Screen doped-polymer materials for electronic Kerr coefficient at 532 nm

The critical path begins with proving the guide geometry and measuring its loss; only then can cascade feasibility be assessed. Nonlinear mechanisms require independent material validation.
