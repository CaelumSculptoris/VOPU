# Architectural Addendum: Distributed 3D Volume Holography in VOPU

**Document Version:** REV8.6 — Hollow-Core Channels & Reflective Nodes
**System:** Volumetric Optical Processing Unit (VOPU)  
**Classification:** Core System Architecture Specification  

---

## Executive Summary

This addendum updates the core VOPU architectural documentation to establish its theoretical foundation as a **Distributed 3D Volume Hologram**, grounded in sub-diffraction hydrogel fabrication (*Yang et al., Nature Photonics 2026*) and linear optical neuromorphic processing (*Wanjura & Marquardt, Nature Physics 2024*; *Yildirim et al., Nature Photonics 2024*). It distinguishes two ImpCarv-written structures: elongated vacancy cavities that define hollow optical routes, and localized dopant-mediated metallic features proposed as reflective computation nodes. Their optical performance and process compatibility remain to be measured.

While traditional optical computing approaches rely either on planar 2D photonic integrated circuits (PICs) or flat 2D diffractive holographic plates (*Lin et al., Science 2018*), VOPU distributes optical interactions across a three-dimensional volume. Neural-network weights are proposed to be compiled into hollow routing cavities and localized reflective nodes. Channel confinement, node reflectivity, propagation loss, and scalability remain device-level hypotheses until measured.

---

## 1. The Distributed 3D Holography Paradigm

### 1.1 From Flat Holograms to Volumetric Node Networks
In conventional volume holography, a single continuous plate or emulsion records interference fringes. Reconstructing the field requires illuminating the entire plate, which introduces severe angular crosstalk and limits the system to single-pass matrix operations.

VOPU breaks the flat surface into a **spatially distributed 3D node mesh**:
1. **Targeted Spatial Transport (design hypothesis):** Two-photon patterning creates elongated hollow cavities rather than isolated spherical vacancies to define 3D routes. The intended mode propagates in the lumen; surrounding vacancy geometry is proposed to provide hollow-core confinement (Section 1.2).
2. **Localized Reflective Nodes (design hypothesis):** A localized dopant-mediated reaction during two-photon exposure is proposed to form a metallic reflective feature. Its shape and orientation set the reflected/scattered field and therefore the node's complex transfer coefficient:
   $$S_i = a_i e^{i\phi_i}$$
3. **Volumetric Field Reconstruction:** As coherent light passes through sequential node layers across the 3D volume, the scattered wavelets overlap and interfere constructively and destructively. The optical field emerging at the output photodetector array represents the reconstructed solution to the compiled path integral equation (*Chen et al., Adv. Intell. Syst. 2023*).

```
       FLAT 2D HOLOGRAPHIC PLATE                 DISTRIBUTED 3D VOPU HOLOGRAPHIC MESH
┌───────────────────────────────────────┐   ┌───────────────────────────────────────────┐
│ Input Beam ──► [ 2D Diffractive Plate ]│   │ Input Wavefront ──► [ 3D Waveguide Bus ]  │
│                       │               │   │                            │              │
│            Single-Pass Diffraction    │   │      Cascaded 3D Micro-Hologram Mesh      │
│            (High Angular Crosstalk)   │   │      [Node] ──► [Node] ──► [Node]         │
└───────────────────────┬───────────────┘   └────────────────────────────┬──────────────┘
                        ▼                                                ▼
            1-Layer Matrix Product                Proposed optical operation + decoder
```

### 1.2 Elongated ImpCarv cavities as optical channels

The selected VOPU routing mode propagates **inside the hollow cavity**. Two-photon vacancy patterning traces a continuous elongated lumen through the hydrogel instead of writing a sequence of isolated spherical vacancies. The channel is the cavity itself, and its boundary is part of the optical design—not a separately polymerized core.

The water-jet experiment is a useful demonstration that an interface can guide light without a conventionally drawn fiber. In the jet, light is in the higher-index water and TIR reflects it from the lower-index air boundary. VOPU also uses a deliberately patterned material boundary, but the selected final geometry puts light inside a gas-filled cavity surrounded by higher-index hydrogel (approximately $n\sim1$ in the cavity versus $n\sim1.5$ in the cited dehydrated gel). This large index contrast changes the field and produces Fresnel reflection, but the index ordering does **not** yield ordinary TIR back into the low-index lumen: TIR at this interface applies to rays in the hydrogel incident toward the cavity, not rays in the cavity incident toward the hydrogel. Therefore the final hollow-core channel must be analyzed as a leaky/open optical structure unless its geometry supplies additional confinement. Antiresonant/inhibited coupling or photonic-bandgap confinement are candidate mechanisms demonstrated in purpose-designed hollow-core fibers; transfer to an ImpCarv cavity remains a VOPU hypothesis. This distinction does not reject the cavity channel: it identifies what the patterned cavity boundary must accomplish and what the first optical measurement must test.

**Proposed first VOPU implementation [H]:** use ImpCarv's elongated vacancy patterning to write a continuous lumen that is liquid-filled during development and washing; solvent exchange, ionic shrinkage, and supercritical-CO2 drying are intended to remove that liquid. The intended operating channel is the resulting gas-filled cavity; surrounding patterned cavities and remaining hydrogel webs may provide antiresonant confinement. Compare a plain lumen with these structured cavity boundaries. A periodic vacancy arrangement could be tested separately as a photonic-bandgap design. Sweep lumen diameter, web thickness, cavity spacing, and operating wavelength with vector-mode/FDTD calculations using measured post-process indices and shrinkage geometry. The reported index difference ($n_\mathrm{gel}-n_\mathrm{gas}\sim0.5$) establishes strong material contrast, not by itself a TIR-guided hollow mode or a low-loss channel.

**Fabrication and validation sequence**
1. Two-photon pattern continuous elongated vacancy paths in the swollen hydrogel; document exposure conditions and pre-shrink cavity geometry.
2. Develop/wash to remove solubilized cleavage products and process residues while the cavities remain liquid-filled. Ensure test channels are open to the wash/exchange fluid, and record wash chemistry and exchange sequence; do not assume sealed cavities can be flushed.
3. Apply the formulation-specific ionic dehydration/shrinkage, solvent exchange, and supercritical-CO2 drying. The target final state is a liquid-free, gas-filled cavity in the shrunken hydrogel; verify residual-solvent removal and that the lumen did not collapse or seal.
4. Measure the complex refractive indices of the final hydrogel and gas, then verify post-process lumen continuity and cross-section.
5. Measure near-field mode profile to confirm power in the lumen, wavelength-dependent confinement/leakage, phase stability, and transmission versus length (cutback). Compare a plain lumen with structured surrounding-cavity boundaries.
6. Add bends and reflective nodes only after a straight hollow-core channel passes pre-registered mode and loss criteria.

If the hollow-core route does not meet the requirements, a solid-core polymer guide is a fallback rather than the assumed VOPU geometry. Panusa et al. demonstrated 5-cm polymer guides written by two-photon polymerization in PDMS, with index contrast on the order of 0.005 and 0.1 dB/cm loss at 710 nm; these results are a process benchmark, not expected ImpCarv-channel performance.

### 1.3 Dopant-mediated reflective computation nodes

The proposed node is separate from the routing cavity. The concept is to load the hydrogel precursor with a suitable metal-ion/dopant chemistry, then use localized two-photon exposure to trigger reduction or another chemical conversion only at the selected node volume. The resulting metallic microfeature would be patterned with a designed reflective face/orientation so its surface normal, local refractive indices, and incident angle determine the directed reflected/scattered field.

This is a fabrication hypothesis, not yet a VOPU material recipe. Two-photon/multiphoton photoreduction of gold inside a specific fluorophore-containing hydrogel has been reported (Machida et al., 2021), establishing a relevant precedent for localized metal formation in a gel. It does not establish the proposed VOPU dopant, a reflective surface, its efficiency, or compatibility with ImpCarv shrinkage. Characterize composition and conversion, feature geometry and roughness, wavelength-dependent complex index/reflectance, angular scattering pattern, absorption, and survival through post-processing before assigning node coefficients $S_i=a_i e^{i\phi_i}$.

In the proposed integrated process, metal precursor would be localized at selected node coordinates and two-photon exposure would convert it into metallic particles or a reflective feature, while liquid is removed from the routed cavity during washing and drying. This sequence is a design hypothesis: demonstrate that the metal product forms at the intended locations, survives subsequent washing/shrinkage/drying, and has the required reflectance and angular response before assuming an integrated channel-node process.

---

## 2. Mathematical Formulation

### 2.1 Continuous Volume Diffraction Integral
The optical field $\mathbf{E}_{\text{out}}(\mathbf{r})$ at any spatial coordinate within the VOPU volume is governed by the volume scattering Lippmann-Schwinger equation:

$$\mathbf{E}_{\text{out}}(\mathbf{r}) = \mathbf{E}_{\text{in}}(\mathbf{r}) + \int_{V} \mathbf{G}(\mathbf{r}, \mathbf{r}') \cdot \left[ k_0^2 \Delta n^2(\mathbf{r}') \right] \mathbf{E}_{\text{total}}(\mathbf{r}') \, d^3\mathbf{r}'$$

Where:
* $\mathbf{G}(\mathbf{r}, \mathbf{r}')$ is the dyadic Green's function representing 3D spatial optical propagation.
* $\Delta n^2(\mathbf{r}')$ is the compiled 3D refractive index distribution written via Implosion Carving (ImpCarv).
* $\mathbf{E}_{\text{in}}(\mathbf{r}')$ is the input optical wavefront injected via Spatial Light Modulator (SLM) or laser array.

### 2.2 Discretized Path Integral Tensor Mapping
When discretized into bounded waveguide channels and terminal scattering nodes, the continuous field reconstruction simplifies to a tensor path integral summation over $N$ discrete optical paths $p$:

$$E_{\text{out}, k} = \sum_{p \in \text{Paths}(j \to k)} \left( \prod_{m \in p} S_m \right) E_{\text{in}, j} e^{i \Delta \Phi_p}$$

Where $S_m = a_m e^{i \phi_m}$ represents the local weight multiplication at node $m$, and $\Delta \Phi_p$ is the accumulated propagation phase along path $p$.

---

## 3. Comparative Architectural Matrix

| Feature / Property | 2D Planar PICs (e.g., MZI Meshes) | Flat 2D Holographic Plates | Distributed 3D VOPU Hologram |
| :--- | :--- | :--- | :--- |
| **Medium Topology** | Flat 2D Silicon / LNOB Wafer | Flat 2D Surface / Thin Film | Monolithic 3D hydrogel/glass; guided paths remain a fabrication hypothesis |
| **Interaction Primitive** | Waveguide Phase Shifters | Surface Diffraction | 3D Volumetric Wave Scattering |
| **Routing Limits** | 2D crossings require design management | Angular crosstalk depends on design | 3D paths may reduce planar crossing constraints; VOPU crosstalk and routing remain unmeasured |
| **Weight Encoding** | Active voltage/heat | Fixed surface grating | Proposed 3D index landscape and calibrated local scattering structures |
| **Cascability & Depth** | Set by device architecture | Set by optical design | Multi-layer depth is a target; no VOPU cascade depth is demonstrated |
| **Complex Weights ($\mathbb{C}$)**| Architecture-dependent | Often phase/amplitude constrained | Intended encoding in measured complex transfer coefficients; not yet validated |

---

## 4. Wavefront Injection & Dynamic Adaptation

### 4.1 Prompt-derived input encoding and wavefront injection
A prompt is not sent into the hydrogel as text. A digital front end first tokenizes it and computes the numerical feature vector required by a selected, bounded model operation. An optical encoder then maps those values to calibrated amplitudes and phases across input ports or spatial modes. With coherent illumination, an SLM or equivalent modulator prepares the input field $\mathbf{E}_{\text{in}}$ to match the fabricated device's measured input basis.

The input field is the runtime payload; the fabricated geometry and calibrated node responses are the fixed analog weights. The optical carrier and its interference do not independently tokenize, interpret, or generate language. Encoding precision, port mapping, and repeatability are system requirements to measure.

### 4.2 Optical operation, readout, and decoding
In a calibrated linear regime, the volume applies a transfer operator that can be written $\mathbf{E}_{\text{out}} = T\mathbf{E}_{\text{in}}$. The operator is intended to arise from propagation through the channel network, local complex scattering, and coherent summation of path contributions. Nonlinear or stateful behavior may modify this mapping only if separately demonstrated. Existing work on nonlinear processing with linear optics motivates possible system strategies; it does not show that VOPU's specific materials or nodes implement those strategies.

Detectors measure output intensity and, where required by the task, phase via coherent readout. Software uses calibration to reconstruct the numerical result, then maps it to the next operation's inputs or output scores/tokens. Direct intensity detection alone does not generally recover an arbitrary complex field. A language-model inference loop would require repeated optical operations and digital preprocessing/readout/decoding unless a complete optical implementation of those stages were independently demonstrated.

The static weight configuration is distinct from runtime input: prompts alter the encoded field, not the fabricated structure. Candidate state-adaptive mechanisms include detection-mediated nonlinear system architectures and material zones such as RSA, excited-state lifetime effects, or XPM. Their suitability, strength, speed, integration, and compatibility with the ImpCarv process remain open experimental questions; none should be described as a working VOPU activation or attention operation until measured.

---

## 5. Engineering Calibration & Phase Budget

Because VOPU operates as a phase-coherent volume hologram, spatial phase accuracy governs the path integral fidelity:
* **Current Phase Uncertainty:** Fabrication tolerances ($\pm 12\text{ nm}$) introduce $\sim 16.4^\circ$ of phase error per node.
* **Holographic Compensation Requirement:** Before estimating useful cascade depth, measure propagation, bend, node, and phase errors on the fabricated guide. The compiler may then apply calibrated phase pre-distortion for systematic optical-path variations; deep-volume performance is not established by the current fabrication tolerance alone.

---

## References & Supporting Literature

1. **Yang, Q., Yang, G., Nambara, T., et al.** (2026). *Isotropic shrinkage of patterned vacancies enables three-dimensional nanoprecise metastructures for visible light applications*. Nature Photonics, 20, 653–663. [doi:10.1038/s41566-026-01896-1](https://doi.org/10.1038/s41566-026-01896-1).
2. **Yildirim, M., Dinc, N. U., Oguz, I., Psaltis, D., & Moser, C.** (2024). *Nonlinear processing with linear optics*. Nature Photonics, 18, 1076–1083.
3. **Wanjura, C. C., & Marquardt, F.** (2024). *Fully nonlinear neuromorphic computing with linear wave scattering*. Nature Physics, 20, 1434–1441.
4. **Onodera, T., McMahon, P. L., et al.** (2024). *Scaling on-chip photonic neural processors using arbitrarily programmable wave propagation*. arXiv:2402.17750.
5. **Chen, R., Tang, Y., Ma, J., & Gao, W.** (2023). *Scientific computing with diffractive optical neural networks*. Advanced Intelligent Systems, 5, 2200536.
6. **Lin, X., Rivenson, Y., Yardimci, N. T., Veli, M., Luo, Y., & Ozcan, A.** (2018). *All-optical machine learning using diffractive networks*. Science, 361(6406), 1004–1008.
7. **Nilsson, T., Wagner, F., Housh, R., & Richerzhagen, B.** (2004). *Scribing of GaN wafer for white LED by water-jet-guided laser*. SPIE Proceedings 5366, 200. [doi:10.1117/12.529012](https://doi.org/10.1117/12.529012).
8. **Risk, W. P., Kim, H.-C., Miller, R. D., Temkin, H., & Gangopadhyay, S.** (2004). *Optical waveguides with an aqueous core and a low-index nanoporous cladding*. Optics Express, 12(26), 6446–6455. [doi:10.1364/OPEX.12.006446](https://doi.org/10.1364/OPEX.12.006446).
9. **Panusa, G., Pu, Y., Wang, J., Moser, C., & Psaltis, D.** (2020). *Fabrication of Sub-Micron Polymer Waveguides through Two-Photon Polymerization in Polydimethylsiloxane*. Polymers, 12(11), 2485. [doi:10.3390/polym12112485](https://doi.org/10.3390/polym12112485).
10. **Oran, D., Rodriques, S. G., Gao, R., et al.** (2018). *3D nanofabrication by volumetric deposition and controlled shrinkage of patterned scaffolds*. Science, 362(6420), 1281–1285. [doi:10.1126/science.aau5119](https://doi.org/10.1126/science.aau5119).
11. **Wang, Y., Huang, C.-J., Jonas, U., Wei, T., Dostalek, J., & Knoll, W.** (2010). *Biosensor based on hydrogel optical waveguide spectroscopy*. Biosensors and Bioelectronics, 25(7), 1663–1668. [doi:10.1016/j.bios.2009.12.003](https://doi.org/10.1016/j.bios.2009.12.003).
12. **Cregan, R. F., Mangan, B. J., Knight, J. C., et al.** (1999). *Single-mode photonic band gap guidance of light in air*. Science, 285(5433), 1537–1539. [doi:10.1126/science.285.5433.1537](https://doi.org/10.1126/science.285.5433.1537).
13. **Argyros, A., Birks, T. A., Leon-Saval, S. G., et al.** (2008). *Antiresonant reflection and inhibited coupling in hollow-core square lattice optical fibres*. Optics Express, 16(8), 5642. [doi:10.1364/OE.16.005642](https://doi.org/10.1364/OE.16.005642).
14. **Machida, S., et al.** (2021). *Anionic fluorophore-assisted fabrication of gold microstructures inside a hydrogel by multi-photon photoreduction*. Optical Materials Express, 11(1), 48. [doi:10.1364/OME.412066](https://doi.org/10.1364/OME.412066).

---

*End of Architectural Addendum REV8.6*
