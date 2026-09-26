# VOPU Research Project

**Volumetric Optical Processing via Sub-Diffraction Implosion Carving**

This repository organizes the research program proposed in
[`VOPU_Architectural_Paper_REV8.pdf`](./VOPU_Architectural_Paper_REV8.pdf).
The goal is to turn the architectural concept into a testable, evidence-driven research project.

## Research objective

Determine whether a monolithic, three-dimensional photonic volume fabricated by Implosion Carving can perform useful linear and nonlinear inference through directed scattering and path integral summation of optical fields, while meeting practical limits on phase fidelity, fabrication precision, scattering efficiency, and cost.

## Core principle

VOPU is not a lossy photonic circuit. It is a volumetric optical computer where:

1. **Waveguide channels are fiber-optic paths** carved into a transparent medium. Propagation loss is negligible — the same physics as fiber optics.
2. **Terminal nodes are computing elements, not loss elements.** Each node scatters light in a directed pattern that implements a weight. The directed scattering IS the computation.
3. **Path integral summation is the accumulation mechanism.** The scattered fields from all nodes sum via optical interference at the output. The interference pattern IS the inferred result.
4. **Nonlinear zones provide state adaptivity.** RSA zones threshold (below threshold they are transparent), excited-state relaxation provides temporal context, and XPM provides dynamic operand interaction.

The only real optical losses are: material absorption at nodes (small fraction), coupling at input/output facets, and undesired scattering into wrong modes. Directed scattering, propagation, and interference are computation — not loss.

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
**Evidence level:** architectural specification grounded in the ImpCarv fabrication demonstration; the compiled weight map, guided 3D bus, terminal nodes, and passive state mechanisms remain research validations. Baseline simulations confirm that a 5-10 node linear demonstrator is feasible — propagation loss is negligible (fiber-like), and directed scattering at nodes is the computational mechanism, not a loss source.  
**Next gate:** compile a minimal weight tensor into a shrinkage-compensated linear routing demonstrator and validate scattering efficiency and phase fidelity with simulation

## Working principles

1. **Directed scattering is computation, not loss.** Terminal nodes scatter light in directed patterns that implement weights. The path integral summation of scattered fields IS the inference. Do not treat computational scattering as insertion loss.
2. **Propagation is fiber-optic.** Waveguide channels in a transparent medium are fiber optics. Propagation loss is negligible and is not a primary engineering concern.
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
