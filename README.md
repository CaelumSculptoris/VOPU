# VOPU Research Project

**Volumetric Optical Processing via Sub-Diffraction Implosion Carving**

This repository organizes the research program proposed in
[`VOPU_Architectural_Paper_REV8.pdf`](./VOPU_Architectural_Paper_REV8.pdf).
The goal is to turn the architectural concept into a testable, evidence-driven research project.

## Research objective

Determine whether a monolithic, three-dimensional photonic volume fabricated by Implosion Carving can perform useful linear and nonlinear inference through directed scattering and path integral summation of optical fields, while meeting practical limits on phase fidelity, fabrication precision, scattering efficiency, and cost.

## Core principle

VOPU is a proposed hybrid optical/electronic inference system: software converts prompt text into numerical features, an optical encoder maps those features onto a coherent laser field, a fabricated volume applies a calibrated analog operation, and detectors plus software decode the result. The physical volume is intended to store fixed weights; prompts change the input field rather than reprogramming those weights.

At the physical level:

1. **ImpCarv channels are elongated hollow cavities.** The cavities are liquid-filled during washing; solvent exchange, ionic shrinkage, and supercritical-CO2 drying are intended to remove the liquid and leave gas-filled lumens. The mode is intended inside the final cavity. Since the gas core is lower-index than the surrounding gel, hollow-mode confinement and propagation loss must be measured rather than inferred from index contrast alone.
2. **Terminal nodes are computing elements, not loss elements.** Each node scatters light in a directed pattern that implements a weight. The directed scattering IS the computation.
3. **Path integral summation is the accumulation mechanism.** The scattered fields from all nodes sum via optical interference. The measured output is an analog result for the compiled operation; software interprets it. Interference alone is not language understanding or a complete transformer.
4. **Nonlinear zones are candidate state-adaptivity mechanisms.** RSA, excited-state relaxation, and XPM may provide thresholding, temporal context, or operand interaction, but their useful response and integration in VOPU remain unvalidated.

The optical budget must account for propagation, bends, coupling, absorption, and parasitic scattering or mode conversion. Deliberate node scattering is the computational operation; only its intended, calibrated output should be counted as computation rather than parasitic loss.

## Project map

| Area | Location | Purpose |
|---|---|---|
| Project definition | [`PROJECT_CHARTER.md`](./PROJECT_CHARTER.md) | Scope, success criteria, assumptions, and boundaries |
| Research plan | [`docs/RESEARCH_PLAN.md`](./docs/RESEARCH_PLAN.md) | Work packages, milestones, and dependencies |
| Architecture | [`docs/ARCHITECTURE.md`](./docs/ARCHITECTURE.md) | System decomposition, signal flow, and computational model |
| Feasibility | [`docs/FEASIBILITY_AND_RISKS.md`](./docs/FEASIBILITY_AND_RISKS.md) | Claims, risks, unknowns, and go/no-go gates |
| Experiments | [`docs/EXPERIMENT_MATRIX.md`](./docs/EXPERIMENT_MATRIX.md) | Experiments, measurements, controls, and exit criteria |
| Literature | [`docs/LITERATURE_MAP.md`](./docs/LITERATURE_MAP.md) | Evidence map and reference-tracking template |
| Concept timeline | [`docs/CONCEPT_DEVELOPMENT_TIMELINE.md`](./docs/CONCEPT_DEVELOPMENT_TIMELINE.md) | Dated provenance, technical milestones, and attribution boundaries |
| Reproducibility | [`docs/REPRODUCIBILITY.md`](./docs/REPRODUCIBILITY.md) | Dataset, simulation, and reporting conventions |
| Decisions | [`docs/DECISION_LOG.md`](./docs/DECISION_LOG.md) | Dated record of project decisions |
| Simulation work | [`simulations/README.md`](./simulations/README.md) | Mode, scattering efficiency, phase, nonlinear, and system models |
| Experimental work | [`experiments/README.md`](./experiments/README.md) | Bench tests and fabrication-validation plans |
| Analysis | [`analysis/README.md`](./analysis/README.md) | Metrics, plots, and quantitative interpretation |

## Current status

**Phase:** project setup and claim validation  
**Evidence level:** architectural specification grounded in the ImpCarv fabrication demonstration; the compiled weight map, hollow-core 3D bus, dopant-mediated reflective nodes, and passive state mechanisms remain research validations. Water-jet and hollow-core fiber results establish related confinement principles, not VOPU-channel loss.
**Next gate:** fabricate and measure a straight, post-shrink hollow-core ImpCarv channel, verifying liquid removal and lumen survival, then validate a dopant-mediated reflective node. Later, test the prompt-to-optical-field and detector-to-numeric-output interfaces on a bounded task.

## Working principles

1. **Calibrated directed scattering is the proposed computation primitive.** Terminal nodes are intended to scatter light in patterns that implement weights. The path integral summation applies a compiled optical operation; prompt inference additionally requires numerical prompt preprocessing, optical encoding, output readout, and decoding. Do not treat intended computational scattering as insertion loss.
2. **Propagation is a measured device property.** The selected hollow lumen uses its cavity/gel boundary as the optical structure; model the hollow mode and candidate antiresonant or photonic-bandgap confinement, then measure propagation, bend, coupling, and mode-mismatch losses after processing.
3. Separate demonstrated results, physical estimates, and hypotheses.
4. Treat passive nonlinearity as a measured device characteristic, not an assumed activation function.
5. Report uncertainty, calibration data, and failed trials.
6. Prefer the smallest experiment that can falsify a claim.
7. Do not use nominal cost estimates as commercial forecasts until throughput, yield, packaging, and capital costs are measured.

## Suggested starting sequence

1. Read [`PROJECT_CHARTER.md`](./PROJECT_CHARTER.md).
2. Review the claim register in [`docs/FEASIBILITY_AND_RISKS.md`](./docs/FEASIBILITY_AND_RISKS.md).
3. Run the baseline calculations described in [`simulations/README.md`](./simulations/README.md).
4. Plan the first routing demonstrator using [`docs/EXPERIMENT_MATRIX.md`](./docs/EXPERIMENT_MATRIX.md).
5. Record all decisions and revisions in [`docs/DECISION_LOG.md`](./docs/DECISION_LOG.md).
