# VOPU Baseline Simulation Report (Revised)

**Date:** 2026-09-26  
**Evidence level:** S (simulated) for all results; D (demonstrated) for literature-validated parameters  
**Author:** Perplexity Computer (automated analysis)

---

## Executive Summary

This report presents the first quantitative baseline physics analysis for the VOPU architecture, revised to reflect the correct computational model: VOPU computes through directed scattering and path integral summation, not through lossy photonic interconnects.

**Key finding:** A 5-10 node linear demonstrator is feasible. Propagation loss through waveguide channels is negligible (fiber-like). The binding constraint on cascade depth is phase error from fabrication tolerance (±12 nm ImpCarv precision), not optical loss. Terminal nodes are computing elements — their directed scattering IS the weight multiplication. The only real losses are material absorption (small fraction) and coupling at input/output facets.

**Go/No-Go recommendation:** Proceed to linear routing demonstrator (WP2). The linear network is feasible at 5-10 node depth.

---

## 1. Mode Analysis [S]

### Single-mode condition

| Parameter Set | n_core | n_clad | NA | Max single-mode diameter |
|---|---|---|---|---|
| VOPU REV8 spec | 1.88 | 1.48 | 1.159 | 351 nm |
| ImpCarv demonstrated | 1.5 | 1.0 | 1.118 | 364 nm |

ImpCarv's demonstrated 67 nm features make single-mode waveguides achievable with margin.

---

## 2. Loss Budget — Corrected [S]

### The fiber-optic principle

VOPU waveguide channels are fiber-optic paths in a transparent medium. Propagation loss is negligible:

| Channel type | Loss | Source |
|---|---|---|
| Silica fiber (1550 nm) | 0.000002 dB/cm | [D] telecom standard |
| PMMA plastic fiber (520 nm) | 0.001 dB/cm | [D] commercial POF |
| ImpCarv hydrogel (532 nm, est.) | 0.011 dB/cm | [E] includes surface roughness |
| REV8 spec placeholder | 0.25 dB/cm | [E] conservative placeholder, not physics |

### Loss breakdown at 10 nodes (corrected model)

| Loss source | Loss | Share | Note |
|---|---|---|---|
| Coupling (in/out) | 0.5 dB | 35% | Getting light into the volume |
| Node absorption | 0.88 dB | 62% | Only absorbed light — directed scattering is computation |
| Propagation | 0.01 dB | 0.8% | Fiber. Negligible. |
| Bends | 0.03 dB | 2% | Small |
| **Total** | **1.4 dB** | | SNR: 78.6 dB |
| Directed scattering | **N/A** | | IS the computation |

### Max cascade depth (loss-limited)

| Scenario | Max depth |
|---|---|
| Fiber-like propagation + node absorption | 706 nodes |
| Optimized nodes + mode-matched coupling | 1,929 nodes |
| Original spec placeholder (0.25 dB/cm) | 561 nodes |

**Loss is NOT the binding constraint.** Even with conservative estimates, loss allows 700+ nodes. The real constraint is phase precision.

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

Binding constraint: **phase error**, not loss. A 5-10 node linear demonstrator is feasible.

---

## 6. Weight Compiler Prototype [S]

A working compiler prototype maps weight matrices to 3D terminal-node topology with inverse shrinkage compensation (5.03× MSF factor) and numerical reference generation.

---

## 7. Recommendations

1. Fabricate and measure a single straight guide (E01) to confirm fiber-like transparency
2. Calibrate one terminal node (E03) to establish directed scattering pattern and efficiency
3. Measure actual ImpCarv dimensional tolerance for VOPU-specific geometries
4. Implement per-node phase calibration to compensate fabrication errors
5. Characterize PbPc-doped hydrogel RSA response at 532 nm in solid state
6. Screen doped-polymer materials for electronic Kerr coefficient at 532 nm

The critical path runs through fabrication precision and nonlinear material characterization. The linear network is feasible; the nonlinear mechanisms require independent material validation.
