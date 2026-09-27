# Decision Log

| Date | Decision | Rationale | Owner | Revisit trigger |
|---|---|---|---|---|
| 2026-09-22 | Start with a linear routing demonstrator before integrated nonlinear inference | Linear propagation and scattering calibration are prerequisites for interpreting nonlinear results | Project team | M1 failure or new fabrication evidence |
| 2026-09-22 | Treat source-paper parameters as provisional inputs | The paper distinguishes estimates and target ranges from demonstrated device data | Project team | Primary-source verification |
| 2026-09-22 | Maintain separate raw, processed, and report artifacts | Prevents analysis drift and supports reproducibility | Project team | Data-management review |
| 2026-09-22 | Treat the REV6 specification as the current end-to-end concept baseline | It defines the weight compiler, inverse-shrinkage workflow, guided 3D optical bus, terminal-node GEMM, passive state mechanisms, and provisional cost model | Project team | Revision of the architectural specification |
| 2026-09-26 | Reframe propagation loss as negligible (fiber-optic principle) | VOPU waveguide channels are fiber-optic paths in a transparent medium. The 0.25 dB/cm in the REV8 spec was a conservative placeholder, not a measured value. Commercial PMMA fiber achieves 0.001 dB/cm at 520nm. Propagation loss should not be treated as a primary engineering concern. | Project team | Measured propagation loss in fabricated VOPU guides |
| 2026-09-26 | Reframe terminal nodes as computing elements, not loss elements | The 0.08 dB/node "insertion loss" was treating the computational operation (directed scattering) as waste. Directed scattering IS the weight multiplication. The path integral summation of scattered fields IS the inference. Only absorbed or mode-mismatched light is actual loss. | Project team | Measured scattering efficiency in fabricated nodes |
| 2026-09-26 | Reframe cascability as phase-precision-limited, not loss-limited | With fiber-like propagation and node-as-computation framing, the binding constraint on cascade depth is phase error from fabrication tolerance (±12 nm ImpCarv precision), not optical loss. Loss budget allows 700+ nodes; phase budget limits to ~7-10 nodes at current tolerance. | Project team | Improved fabrication precision or phase calibration |
| 2026-09-26 | Reframe loss budget around coupling, absorption, and undesired scattering | The real loss terms are: coupling at input/output facets, material absorption at nodes (small fraction), and undesired scattering into wrong modes. These are the optimization targets, not propagation loss or "insertion loss." | Project team | Measured loss breakdown in fabricated device |

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
