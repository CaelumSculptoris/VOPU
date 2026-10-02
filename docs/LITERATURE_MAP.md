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

Optical confinement does not require a conventionally drawn fiber; it requires a suitable optical mode and boundary. VOPU's selected routing features are elongated ImpCarv-written hollow cavities, not isolated spherical nodes, and the intended mode is in the lumen. The cavity/gel index change is central to the optical boundary, but an air-filled cavity is lower-index than hydrogel. Thus the water-jet experiment supports interface-guided transport as an analogy, not ordinary TIR for this reversed index ordering. The current design hypothesis is hollow-core confinement through an engineered antiresonant or photonic-bandgap boundary.

**Primary sources and what they support:**

- **Nilsson, T., Wagner, F., Housh, R., & Richerzhagen, B.** (2004). “Scribing of GaN wafer for white LED by water-jet-guided laser.” *SPIE Proceedings* 5366, 200. https://doi.org/10.1117/12.529012. Demonstrates practical laser delivery using a water jet; it is not a measurement of a static solid channel or VOPU propagation loss.
- **Risk, W. P., Kim, H.-C., Miller, R. D., Temkin, H., & Gangopadhyay, S.** (2004). “Optical waveguides with an aqueous core and a low-index nanoporous cladding.” *Optics Express* 12(26), 6446–6455. https://doi.org/10.1364/OPEX.12.006446. Demonstrates that an aqueous core can be guided when paired with an intentionally lower-index nanoporous cladding; it reinforces the need to engineer the boundary.
- **Panusa, G., Pu, Y., Wang, J., Moser, C., & Psaltis, D.** (2020). “Fabrication of Sub-Micron Polymer Waveguides through Two-Photon Polymerization in Polydimethylsiloxane.” *Polymers* 12(11), 2485. https://doi.org/10.3390/polym12112485. Reports 5-cm 2PP-written polymer guides with index contrast on the order of 0.005 and 0.1 dB/cm loss at 710 nm. This is a useful fabrication benchmark, not a transfer value for ImpCarv hydrogel.
- **Wang, Y., Huang, C.-J., Jonas, U., Wei, T., Dostalek, J., & Knoll, W.** (2010). “Biosensor based on hydrogel optical waveguide spectroscopy.” *Biosensors and Bioelectronics* 25(7), 1663–1668. https://doi.org/10.1016/j.bios.2009.12.003. Demonstrates a planar hydrogel waveguiding geometry, not a low-loss 3D routing bus.
- **Oran, D., Rodriques, S. G., Gao, R., et al.** (2018). “3D nanofabrication by volumetric deposition and controlled shrinkage of patterned scaffolds.” *Science* 362(6420), 1281–1285. https://doi.org/10.1126/science.aau5119. Supports 3D scaffold patterning and shrinkage; it does not report guided-mode propagation loss.
- **Cregan, R. F., Mangan, B. J., Knight, J. C., et al.** (1999). “Single-mode photonic band gap guidance of light in air.” *Science* 285(5433), 1537–1539. https://doi.org/10.1126/science.285.5433.1537. Demonstrates hollow/air-core guidance using a photonic-bandgap cladding, not ordinary TIR at a low-index core/high-index wall.
- **Argyros, A., Birks, T. A., Leon-Saval, S. G., et al.** (2008). “Antiresonant reflection and inhibited coupling in hollow-core square lattice optical fibres.” *Optics Express* 16(8), 5642. https://doi.org/10.1364/OE.16.005642. Demonstrates hollow-core guidance using engineered antiresonant/inhibited-coupling structure, not a plain void in bulk gel.
- **Machida, S., et al.** (2021). “Anionic fluorophore-assisted fabrication of gold microstructures inside a hydrogel by multi-photon photoreduction.” *Optical Materials Express* 11(1), 48. https://doi.org/10.1364/OME.412066. Demonstrates a specific fluorophore-assisted gold-forming chemistry in hydrogel. It does not establish the VOPU dopant recipe, reflective-facet performance, or survival through ImpCarv processing.

**VOPU design hypothesis:** replace isolated vacancy nodes along selected routes with a continuous, elongated hollow lumen. The lumen is liquid-filled during washing; solvent exchange, ionic shrinkage, and supercritical-CO2 drying are intended to remove that liquid and leave a gas-filled channel in the final hydrogel. Verify residue removal and lumen continuity. The intended mode propagates inside the final cavity. The cavity/gel index variation forms the optical boundary, but with gas inside higher-index gel it does not produce ordinary TIR back into the lumen. Test a plain lumen first, then surrounding ImpCarv cavities that leave thin hydrogel webs and may provide antiresonant reflection; separately explore a periodic vacancy boundary if needed for a photonic bandgap. Compare post-shrink vector-mode predictions, near-field imaging, and cutback loss. A two-photon-polymerized solid-core guide remains a process benchmark, not the presumed VOPU geometry.

**Separate node hypothesis:** two-photon-triggered dopant chemistry may form localized metallic reflective facets. Measure conversion chemistry, reflectance, absorption, facet geometry/orientation, and angular scattering; hydrogel photoreduction literature is a specific precedent, not validation of the VOPU formulation.

**Evidence label:** D for the cited guiding/fabrication results in their reported geometries; H for transfer to ImpCarv cavity channels and dopant-mediated reflective nodes; E only for calculations explicitly using measured post-process indices and geometry.

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
