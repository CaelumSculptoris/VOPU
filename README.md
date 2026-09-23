# VOPU Research Project

**Volumetric Optical Processing via Sub-Diffraction Implosion Carving**

This repository organizes the research program proposed in
[`VOPU_Architectural_Paper_REV8.pdf`](/Users/cal/Projects/VOPU/VOPU_Architectural_Paper_REV8.pdf).
The goal is to turn the architectural concept into a testable, evidence-driven research project.

## Research objective

Determine whether a monolithic, three-dimensional photonic volume fabricated by Implosion Carving can perform useful linear and nonlinear inference while meeting practical limits on optical loss, phase fidelity, fabrication yield, and cost.

## Project map

| Area | Location | Purpose |
|---|---|---|
| Project definition | [`PROJECT_CHARTER.md`](./PROJECT_CHARTER.md) | Scope, success criteria, assumptions, and boundaries |
| Research plan | [`docs/RESEARCH_PLAN.md`](./docs/RESEARCH_PLAN.md) | Work packages, milestones, and dependencies |
| Architecture | [`docs/ARCHITECTURE.md`](./docs/ARCHITECTURE.md) | System decomposition and signal flow |
| Feasibility | [`docs/FEASIBILITY_AND_RISKS.md`](./docs/FEASIBILITY_AND_RISKS.md) | Claims, risks, unknowns, and go/no-go gates |
| Experiments | [`docs/EXPERIMENT_MATRIX.md`](./docs/EXPERIMENT_MATRIX.md) | Experiments, measurements, controls, and exit criteria |
| Literature | [`docs/LITERATURE_MAP.md`](./docs/LITERATURE_MAP.md) | Evidence map and reference-tracking template |
| Concept timeline | [`docs/CONCEPT_DEVELOPMENT_TIMELINE.md`](./docs/CONCEPT_DEVELOPMENT_TIMELINE.md) | Dated provenance, technical milestones, and attribution boundaries |
| Reproducibility | [`docs/REPRODUCIBILITY.md`](./docs/REPRODUCIBILITY.md) | Dataset, simulation, and reporting conventions |
| Decisions | [`docs/DECISION_LOG.md`](./docs/DECISION_LOG.md) | Dated record of project decisions |
| Simulation work | [`simulations/README.md`](./simulations/README.md) | FDTD, mode, loss, nonlinear, and system models |
| Experimental work | [`experiments/README.md`](./experiments/README.md) | Bench tests and fabrication-validation plans |
| Analysis | [`analysis/README.md`](./analysis/README.md) | Metrics, plots, and quantitative interpretation |

## Current status

**Phase:** project setup and claim validation  
**Evidence level:** architectural proposal; most performance claims remain to be experimentally demonstrated  
**Next gate:** establish a minimal linear single-mode routing demonstrator and validate the loss/phase budget with simulation

## Working principles

1. Separate demonstrated results, physical estimates, and hypotheses.
2. Treat passive nonlinearity as a measured device characteristic, not an assumed activation function.
3. Report uncertainty, calibration data, and failed trials.
4. Prefer the smallest experiment that can falsify a claim.
5. Do not use nominal cost estimates as commercial forecasts until throughput, yield, packaging, and capital costs are measured.

## Suggested starting sequence

1. Read [`PROJECT_CHARTER.md`](./PROJECT_CHARTER.md).
2. Review the claim register in [`docs/FEASIBILITY_AND_RISKS.md`](./docs/FEASIBILITY_AND_RISKS.md).
3. Run the baseline calculations described in [`simulations/README.md`](./simulations/README.md).
4. Plan the first routing demonstrator using [`docs/EXPERIMENT_MATRIX.md`](./docs/EXPERIMENT_MATRIX.md).
5. Record all decisions and revisions in [`docs/DECISION_LOG.md`](./docs/DECISION_LOG.md).
