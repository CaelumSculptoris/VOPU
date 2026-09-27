# Fabrication

This folder documents design-for-fabrication constraints, shrinkage compensation, material batches, metrology, process windows, and defect classification.

## Required records

- Pre-shrink design geometry and inverse deformation parameters.
- Material formulation and batch identifiers.
- Writing parameters and actual write time.
- Dehydration and drying conditions.
- Post-shrink dimensional metrology.
- Defect inventory and functional yield.

## Fabrication precision is the primary constraint

The binding constraint on VOPU cascade depth is fabrication precision, not loss. ImpCarv's demonstrated ±12 nm lateral tolerance translates to ~13.7° per-node phase uncertainty. Improving this precision, or implementing per-node phase calibration, is the critical path to deeper networks.

## Channel transparency

Fabricated waveguide channels should exhibit fiber-like transparency. If measured propagation loss exceeds ~0.05 dB/cm, investigate surface roughness and material impurities — the medium itself should be transparent at 532 nm.

No fabrication protocol should be treated as approved operating procedure until reviewed for facility, chemical, laser, and pressure-system safety.
