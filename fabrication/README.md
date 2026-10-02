# Fabrication

This folder documents design-for-fabrication constraints, shrinkage compensation, material batches, metrology, process windows, and defect classification.

## Required records

- Pre-shrink design geometry and inverse deformation parameters.
- Material formulation and batch identifiers.
- Two-photon exposure parameters, cleavage/vacancy geometry, and actual write time.
- Developer/wash chemistry and solvent-exchange sequence; cavity state (liquid-filled or gas-filled) at each stage.
- Ionic dehydration/shrinkage conditions, solvent-exchange record, and supercritical-CO2 drying conditions.
- Evidence of residual-solvent removal and post-process cavity state.
- Post-shrink dimensional metrology.
- Defect inventory and functional yield.

## Fabrication precision and guided-channel feasibility

ImpCarv has demonstrated precise vacancy patterning, but useful hollow-channel loss and phase stability have not been measured. Fabrication precision, lumen continuity, post-drying cavity contents, boundary geometry, and propagation loss must all be characterized before identifying the binding constraint on cascade depth.

## Channel transparency

The proposed routing primitive is a continuous, elongated ImpCarv-written cavity. During exposure and washing it is liquid-filled; solvent exchange, ionic shrinkage, and supercritical-CO2 drying are intended to remove the liquid and leave a gas-filled lumen in the final substrate. Through-channels should have accessible openings during washing and solvent exchange; a sealed cavity cannot be assumed to flush. Verify residue removal and lumen continuity rather than assuming liquid removal or cavity survival from the process description alone.

The intended optical mode is in this final lumen. The cavity/gel boundary has a large index contrast (reported gel $n\sim1.5$ versus gas $n\sim1$), but this contrast alone does not provide TIR back into a lower-index hollow core. Test whether the cavity shape, including candidate surrounding vacancies/webs, gives hollow-core confinement. Measure the final mode and propagation loss; 0.05 dB/cm is an aspirational target only if pre-registered, not an assumed material property.

Reflective computation nodes are a separate proposed process: two-photon-triggered dopant chemistry may form oriented metallic facets. Do not assume metal formation or reflectivity from the presence of a dopant; characterize the reaction product and wavelength-dependent optical response independently.

No fabrication protocol should be treated as approved operating procedure until reviewed for facility, chemical, laser, and pressure-system safety.
