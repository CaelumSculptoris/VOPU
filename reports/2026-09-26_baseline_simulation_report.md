# VOPU Baseline Simulation Report

**Date:** 2026-09-26  
**Evidence level:** S (simulated) for all results; D (demonstrated) for literature-validated parameters  
**Author:** Perplexity Computer (automated analysis)

---

## Executive Summary

This report presents the first quantitative baseline physics analysis for the VOPU architecture. It addresses the project's next gate: validating the loss/phase budget with simulation and demonstrating a minimal weight compiler.

**Key finding:** A 5-10 node linear demonstrator is feasible within current loss and phase budgets. The binding constraint is phase error from fabrication tolerance (±12 nm ImpCarv lateral precision), which limits cascade depth to ~7 nodes at 45° tolerance. The nonlinear XPM mechanism requires material engineering (doped polymer or nanoparticle enhancement) to achieve detectable Q/K interaction.

**Go/No-Go recommendation:** Proceed to linear routing demonstrator (WP2). Defer nonlinear integration (WP4) until material characterization is complete.

---

## 1. Mode Analysis [S]

### Single-mode condition

| Parameter Set | n_core | n_clad | NA | Max single-mode diameter |
|---|---|---|---|---|
| VOPU REV8 spec | 1.88 | 1.48 | 1.159 | 351 nm |
| ImpCarv demonstrated | 1.5 | 1.0 | 1.118 | 364 nm |

With the VOPU's high index contrast (Δn = 0.40, NA = 1.16), single-mode waveguides must be smaller than ~351 nm diameter. ImpCarv has demonstrated 67 nm lateral features, making this achievable with margin.

**Literature comparison:** LNOI waveguides achieve 0.13 dB/cm propagation loss with ~466 nm width at 1550 nm ([arXiv:2006.11562](https://arxiv.org/abs/2006.11562)). The VOPU target of 0.25 dB/cm at 532 nm is aggressive but within the demonstrated range of high-quality waveguide fabrication.

---

## 2. Loss Budget [S]

### Cascade depth limits (SNR-based, 15 dB required SNR, 10 mW laser, -70 dBm noise floor)

| Scenario | WG attenuation (dB/cm) | Node loss (dB) | Max cascade depth |
|---|---|---|---|
| VOPU REV8 target | 0.25 | 0.08 | 614 nodes |
| Conservative (planar-like) | 1.0 | 0.12 | 293 nodes |
| Pessimistic (fs-written) | 3.0 | 0.15 | 143 nodes |
| Best case (LNOI-grade) | 0.13 | 0.05 | 1024 nodes |

**Loss per node:** 0.33 dB (optimistic) to 0.45 dB (conservative), dominated by node insertion loss (0.08 dB) rather than propagation (0.025 dB per 500 µm hop).

**Finding:** Loss is NOT the binding constraint. Even pessimistic estimates allow 143 nodes, far exceeding the phase-limited depth. The dominant optimization target is reducing node insertion loss.

---

## 3. Phase Error Budget [S]

### Per-node phase error breakdown (node-scale, not path-scale)

| Error Source | Per-node σ (radians) | Per-node σ (degrees) | Fraction of total |
|---|---|---|---|
| Fabrication tolerance (±12 nm) | 0.239 | 13.7° | 68% |
| Node scattering variation (±5%) | 0.157 | 9.0° | 29% |
| Index variation (±1% of Δn) | 0.024 | 1.4° | <1% |
| Thermal node drift (±0.5 K) | ~0 | ~0° | <1% |
| **Total per-node** | **0.287** | **16.4°** | **100%** |

### Cascade depth limits (phase-based)

| Tolerance | Max depth |
|---|---|
| 45° (loose) | 7 nodes |
| 22.5° (strict) | 2 nodes |
| 10° (very strict) | 0 nodes |

**Finding:** Fabrication tolerance is the dominant phase error source (68%). The ±12 nm ImpCarv lateral precision translates to ±13.7° per-node phase uncertainty. This is the binding constraint on cascade depth.

**Path thermal drift:** The inter-node path thermal drift is ~28.8° per 0.5 K, but this is a systematic phase offset that can be measured and calibrated during initialization. It does not accumulate as √N.

---

## 4. Nonlinear Mechanism Estimates [S, with D literature parameters]

### 4a. RSA Epsilon-Thresholding

| Parameter | Value | Source |
|---|---|---|
| Material | PbPc(β-CP)4 in CHCl3 | [D] Shirk 1996 |
| Wavelength | 532 nm | [D] |
| Threshold fluence | 0.07 J/cm² (8 ns pulse) | [D] |
| Threshold intensity | 8.75 MW/cm² | [D] |
| Power in 500 nm guide | ~17 mW | [E] |
| Extinction ratio | ~18 dB | [E] |

**Finding:** RSA thresholding is feasible. PbPc at 532 nm has demonstrated thresholding at 0.07 J/cm². In a 500 nm VOPU waveguide, this corresponds to ~17 mW guided power, well within the range of available 532 nm lasers. Caveat: this is for solution-phase; solid-state hydrogel doping may shift the threshold.

### 4b. Excited-State Lifetime (Lambda-Decay)

| Parameter | Value | Source |
|---|---|---|
| VOPU reference τ | 1.2 ns | [E] VOPU spec |
| ZnPc S1 lifetime | 2.88 ns | [D] Savolainen 2007 |
| ZnPc triplet lifetime | 220 ns | [D] |
| Phthalocyanine film | 67 ps | [D] pump-probe |
| Temporal context window (3τ) | 3.6 ns (VOPU) | [E] |

**Finding:** The VOPU 1.2 ns reference is shorter than typical ZnPc S1 (2.88 ns) but plausible for doped hydrogel environments where lifetimes shorten. The 3.6 ns temporal context window means sequential pulses within this window would interact via excited-state memory. Triplet states (220 ns) could cause unwanted persistent absorption.

### 4c. Cross-Phase Modulation (XPM)

| Material | n2 (m²/W) | Power for 45° phase shift | Feasibility |
|---|---|---|---|
| Silicon | 3×10⁻¹⁸ | 4.4 mW | Not available in hydrogel |
| PMMA (pure) | 1×10⁻¹⁸ | 13,057 mW | Impractical |
| Doped polymer | 1×10⁻¹⁶ | 131 mW | Challenging but possible |
| Hydrogel (thermal) | 1×10⁻¹³ | 0.13 mW | Too slow (µs-ms) |

**Finding:** XPM is the weakest link. Pure PMMA Kerr nonlinearity is too weak (13 W for 45°). Doped polymer with chromophore (n2 ~ 10⁻¹⁶) requires 131 mW, which is high but potentially achievable. Thermal hydrogel nonlinearity is very strong but too slow for ns-scale Q/K interaction. **Recommendation:** Characterize doped polymer or silicon-nanoparticle-doped hydrogel for electronic Kerr response at 532 nm.

---

## 5. Cascability Analysis [S]

### Combined fidelity (loss + phase)

| Fidelity threshold | Max depth |
|---|---|
| 90% fidelity | 10 nodes |
| 50% fidelity | 30 nodes |

### Binding constraint

The binding constraint is **phase error at 22.5° strict tolerance** (2 nodes). At the more relaxed 45° tolerance, phase allows 7 nodes. Loss allows 614+ nodes. The nonlinear mechanism (XPM) requires material engineering but does not gate the linear network.

### Go/No-Go assessment

| Gate | Result | Rationale |
|---|---|---|
| Proceed to linear demonstrator (WP2) | **GO** | 5-10 node linear network is feasible |
| Proceed to integrated nonlinear tests (WP4) | **CONDITIONAL** | XPM requires material breakthrough; RSA is feasible |
| Proceed to deeper networks (WP3) | **CONDITIONAL** | Phase error must be reduced below 10° per node |
| Publish performance claim | **NO** | Requires measured data, not simulation only |

---

## 6. Weight Compiler Prototype [S]

A minimal weight compiler has been implemented (`compiler/weight_compiler.py`) that:

1. Accepts a weight matrix (e.g., 4×4 Wq layer)
2. Maps weights to complex terminal-node scattering coefficients (amplitude + phase encoding)
3. Synthesizes a 2D node grid topology with Manhattan routing
4. Applies inverse shrinkage compensation (factor 5.03×, MSF formulation)
5. Computes a numerical reference (expected optical output)
6. Emits a design file with all fabrication artifacts

**Example output:** 4×4 weight matrix → 16 terminal nodes with pre-shrink coordinates (5.03× expansion applied), complex transfer matrix computed for calibration comparison.

---

## 7. Recommendations

### Immediate (WP2 - Linear Primitive)
1. Fabricate and measure a single straight guide (E01) to validate the 0.25 dB/cm target
2. Calibrate one terminal node (E03) to establish phase error baseline
3. Measure the actual ImpCarv dimensional tolerance for VOPU-specific geometries

### Short-term (WP3 - Scaling)
4. Reduce fabrication phase error below 10° per node (requires <8 nm tolerance or active calibration)
5. Implement per-node phase calibration to compensate systematic fabrication errors
6. Demonstrate a 5-node cascade with measured transfer matrix

### Medium-term (WP4 - Nonlinear)
7. Characterize PbPc-doped hydrogel RSA response at 532 nm in solid state
8. Screen doped-polymer and nanoparticle-doped hydrogel for electronic Kerr coefficient at 532 nm
9. Measure excited-state lifetime of selected chromophore in hydrogel matrix

### Critical path
The critical path to a useful VOPU demonstrator runs through **fabrication precision** and **nonlinear material characterization**. The linear network is feasible at 5-10 node depth; the nonlinear mechanisms require independent material validation before integration.

---

## 8. Literature Sources

| Source | Key parameter | URL |
|---|---|---|
| Yang et al., Nature Photonics 2026 | ImpCarv fabrication: 67±12 nm features, Δn≈0.5 | [DOI:10.1038/s41566-026-01896-1](https://doi.org/10.1038/s41566-026-01896-1) |
| Shirk et al., 1996 | PbPc RSA threshold: 0.07 J/cm² at 532 nm | [IOPscience](https://iopscience.iop.org) |
| Savolainen et al., 2007 | ZnPc S1 lifetime: 2.88 ns | [University of Twente](https://ris.utwente.nl) |
| Agrawal lecture | n2(Si)=3×10⁻¹⁸ m²/W, γ~10 W⁻¹km⁻¹ | [U. Rochester](https://labsites.rochester.edu/agrawal/) |
| LNOI waveguide study | 0.13 dB/cm propagation loss | [arXiv:2006.11562](https://arxiv.org/abs/2006.11562) |
| Hydrogel NLO study | n2~10⁻⁹ cm²/W (thermal) | [Multiphysics Journal](https://www.themultiphysicsjournal.com) |
