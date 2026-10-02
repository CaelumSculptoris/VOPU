# Decision Log

| Date | Decision | Rationale | Owner | Revisit trigger |
|---|---|---|---|---|
| 2026-09-22 | Start with a linear routing demonstrator before integrated nonlinear inference | Linear propagation and scattering calibration are prerequisites for interpreting nonlinear results | Project team | M1 failure or new fabrication evidence |
| 2026-09-22 | Treat source-paper parameters as provisional inputs | The paper distinguishes estimates and target ranges from demonstrated device data | Project team | Primary-source verification |
| 2026-09-22 | Maintain separate raw, processed, and report artifacts | Prevents analysis drift and supports reproducibility | Project team | Data-management review |
| 2026-09-22 | Treat the REV6 specification as the current end-to-end concept baseline | It defines the weight compiler, inverse-shrinkage workflow, guided 3D optical bus, terminal-node GEMM, passive state mechanisms, and provisional cost model | Project team | Revision of the architectural specification |
| 2026-09-26 | Historical: reframe propagation loss as negligible (superseded 2026-10-01) | Earlier rationale: VOPU waveguide channels were assumed to have negligible loss by analogy with commercial fiber. This did not establish a suitable VOPU core/cladding structure or its propagation loss. | Project team | Superseded; see 2026-10-01 decision and E01 |
| 2026-09-26 | Reframe terminal nodes as computing elements, not loss elements | Historical shorthand described directed scattering and path-integral summation as "the inference." More precisely, they are the proposed optical operation for compiled weights; prompt preprocessing, optical encoding, readout, and decoding are also required for end-to-end inference. Only absorbed or mode-mismatched light is parasitic loss. | Project team | Measured scattering efficiency in fabricated nodes |
| 2026-09-26 | Historical: reframe cascability as phase-precision-limited (superseded 2026-10-01) | Earlier conditional model assumed fiber-like propagation. Actual propagation, phase, and scattering limits must be determined from fabricated devices; the cited cascade depths are not validated performance. | Project team | Superseded; measure guide and node losses |
| 2026-09-26 | Reframe loss budget around coupling, absorption, and undesired scattering | The real loss terms are: coupling at input/output facets, material absorption at nodes (small fraction), and undesired scattering into wrong modes. These are the optimization targets, not propagation loss or "insertion loss." | Project team | Measured loss breakdown in fabricated device |
| 2026-10-01 | Supersede the negligible-propagation-loss assumption; test hollow-core ImpCarv channels | The intended mode is inside a continuous two-photon-written cavity. It is liquid-filled during washing; solvent exchange, shrinkage, and supercritical drying are intended to remove the liquid. The final cavity/gel index boundary defines the optical interaction; with gas core below gel index, ordinary step-index TIR does not confine the hollow mode. Verify process-state contents and test plain and engineered cavity boundaries. | Project team | E01 post-shrink channel measurements |

## Entry template

```text
Date:
Decision:
Options considered:
Rationale:
Evidence:
Owner:
Revisit trigger:
```
