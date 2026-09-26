# Literature Map

## Reading tracks

### Fabrication

Investigate the primary ImpCarv/isotropic-shrinkage work, feature fidelity, shrinkage uniformity, material compatibility, and post-processing limits.

#### Added source: ImpCarv vacancy patterning and visible-light metastructures

**Citation:** Yang, Q., Yang, G., Nambara, T. *et al.* "Isotropic shrinkage of patterned vacancies enables three-dimensional nanoprecise metastructures for visible light applications." *Nature Photonics* 20, 653–663 (2026).  
**DOI/URL:** https://doi.org/10.1038/s41566-026-01896-1  
**Research track:** Fabrication; nanophotonics; optical neural networks.

**What is directly demonstrated:** The authors introduce implosion carving (ImpCarv): two-photon photosensitizer-mediated cleavage of vacancies in swollen hydrogels, isotropic shrinkage using staged cation treatment, and supercritical drying to preserve the resulting geometry. In polyacrylate-based scaffolds they report lateral vacancy widths of 67 ± 12 nm FWHM and axial steps of 22 ± 2 nm. They also demonstrate complex high-aspect-ratio and helical geometries, refractive-index/phase programmability, and a visible-wavelength (532 nm) diffractive device with approximately 500 nm lateral neurons and eight discrete height levels for classification of MNIST digits.

**Relevant parameter values:** HSF and MSF formulations reached final linear shrinkage factors of 13.18 ± 0.28 and 5.03 ± 0.06, respectively, after solvent exchange and supercritical drying. Post-dehydration gel refractive index was approximately 1.5, giving an air-filled vacancy contrast of approximately Δn = 0.5. The demonstrated machine-learning device used two 120 × 120 arrays, 500 × 500 nm lateral neurons, 0–700 nm axial dimensions, and a 532 nm target wavelength.

**Measurement method:** Fluorescence imaging during the swollen and partially shrunken stages; SEM and AFM after dehydration; diffraction phase microscopy and index matching for refractive-index characterization; camera-based output intensity measurements for device evaluation.

**Limitations:** The results are demonstrated for specific hydrogel formulations and process conditions; shrinkage and drying must be re-optimized for other materials. The paper does not establish VOPU's single-mode waveguide transparency, 3D routing fidelity, terminal-node directed scattering patterns, nonlinear response, packaging tolerance, or manufacturing throughput. The optical classifier is a passive diffractive demonstration, not evidence for VOPU's proposed directed-scattering inference substrate.

**How it changes the VOPU claim register:** Upgrade the feasibility basis for sub-100 nm post-shrinkage vacancy fabrication from hypothesis to demonstrated in the cited source, while retaining independent-reproduction and VOPU-specific geometry-to-scattering-transfer tests as open requirements. Use the reported shrinkage factors, feature sizes, index contrast, and phase-control measurements as bounded starting inputs rather than as specifications for VOPU's doped or nonlinear structures.

**Evidence label:** D for the reported ImpCarv fabrication, metrology, and passive visible-light classifier; H/S for transfer to VOPU's directed-scattering architecture.

### Fiber-optic propagation principle

VOPU waveguide channels are fiber-optic paths in a transparent medium. Propagation loss should be treated as negligible, not as a primary engineering concern.

**Supporting evidence:**
- Commercial PMMA plastic optical fiber achieves ~0.1 dB/m (0.001 dB/cm) at 520 nm [D — commercial POF specifications].
- Silica fiber achieves 0.2 dB/km at 1550 nm [D — telecommunications standard].
- ImpCarv hydrogel is transparent at 532 nm; Rayleigh scattering is minimal in a homogeneous polymer.
- Surface roughness from ImpCarv fabrication (±12 nm) adds an estimated ~0.01 dB/cm scattering loss [E].
- Total estimated propagation loss: ~0.011 dB/cm — 23x lower than the REV8 spec's 0.25 dB/cm placeholder.

**How it changes the VOPU claim register:** Reframe propagation loss from a primary risk to a negligible term. The 0.25 dB/cm in the REV8 spec was a conservative placeholder, not a measured value. The real loss terms are coupling, node absorption, and undesired scattering.

**Evidence label:** D for fiber-optic principle; E for VOPU-specific roughness estimate.

### Integrated photonics

Compare 3D waveguide writing, single-mode routing, volumetric interconnects, packaging, and phase stability with planar photonic integrated circuits.

### Optical neural networks

Review diffractive networks, directed scattering, path integral methods, volume holograms, optical nonlinear activations, and photonic transformer demonstrations.

### Nonlinear materials

Focus on RSA cross-sections (transparent below threshold), excited-state kinetics, Kerr/XPM coefficients, nanoparticle enhancement, damage thresholds, and measurement methods.

### Modeling

Review FDTD, coupled-mode theory, directed scattering models, nonlinear rate equations, uncertainty propagation, inverse design, and calibration of complex optical transfer matrices.

## Concept-provenance sources

The following project artifacts document the development of the VOPU concept.
They are provenance records, not independent experimental validation:

- [`IMG_2119.PNG`](../IMG_2119.PNG): dated 28 December 2024 image describing a
  volumetric neural-network substrate, node lattice, Gaussian/GP-kernel
  processing, and interferometric injection/readout.
- [`AI chip breakthrough claim 2.md`](../AI%20chip%20breakthrough%20claim%202.md):
  imported conversation dated 15–16 December 2025 containing the explicit
  waveguide-lattice, weight-encoding, transform-layer, and optical-inference
  formulation.
- [`Steal Me.pdf`](../Steal%20Me.pdf): VOPU architectural specification
  (document ID SPEC-VOPU-2026-REV6), whose file metadata records creation on
  17 September 2026. It defines the compiled latent-graph workflow, inverse
  shrinkage compensation, frozen volumetric weight mapping, terminal-node directed
  scattering, passive epsilon-thresholding, lambda-decay temporal context, and
  dynamic Q/K cross-phase interaction.

## VOPU architectural specification

**Source:** [`Steal Me.pdf`](../Steal%20Me.pdf), SPEC-VOPU-2026-REV6  
**Research track:** Volumetric optical computing; photonic neural networks;
fabrication systems.

**Core proposal:** Compile transformer state-dictionary weights (`Wq`, `Wk`,
`Wv`, and feed-forward weights) into a 3D waveguide topology, terminal-node
map, and refractive-index/material landscape. A monolithic single-mode optical
bus routes phase- and amplitude-encoded fields to terminal nodes that scatter
in directed patterns implementing compiled weights. The scattered fields sum
via path integral at the output.

**State mechanisms:** Reverse-saturable-absorber zones implement proposed
epsilon-thresholding (transparent below threshold); excited-state relaxation
provides proposed lambda-decay temporal context; and Q/K cross-phase modulation
provides a proposed dynamic operand interaction.

**Fabrication workflow:** Two-photon scribing in a swollen polyacrylate
hydrogel, terminal-node functionalization, ionic dehydration and isotropic
shrinkage, supercritical CO2 drying, aligned packaging, and homodyne readout.
The specification explicitly calls for inverse-shrinkage compensation before
writing.

**Economic model:** The document gives a provisional marginal core estimate of
approximately $23.93, including hydrogel, precursors, chromophores,
photoinitiators/solvents, writing, and drying. This is a model input, not a
measured production cost.

**Evidence label:** H for the complete VOPU architecture and its nonlinear
mechanisms; D for the document's own specification; D/S for the separate
ImpCarv fabrication results on which the proposed substrate is based.

## Reference-entry template

```text
Citation:
DOI/URL:
Research track:
What is directly demonstrated:
Relevant parameter values:
Measurement method:
Limitations:
How it changes the VOPU claim register:
Evidence label:
```

The references in the source paper are starting points, not validation by themselves. Each quantitative parameter used in a model must be tied to a source, measurement, or explicitly labeled assumption.
