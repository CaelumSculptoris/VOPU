# Simulation Work

Simulation work should progress from validated linear models to coupled nonlinear models.

## Recommended sequence

1. Scalar and vector mode analysis for post-shrinkage guide geometries.
2. Hollow-core channel design and characterization — include the liquid-filled wash stage and intended gas-filled post-dry geometry; model the elongated lumen and cavity/gel boundary, testing a plain lumen and structured surrounding-cavity geometries for confinement. Derive propagation loss from measured data or sweep it as an explicit uncertainty.
3. Terminal-node directed scattering simulation — model the scattering pattern, scattering efficiency (directed vs. absorbed/mismatched fraction), and complex transfer function.
4. Multi-node path integral accumulation with measured or swept propagation, mode-conversion, scattering, and phase errors.
5. RSA two-level rate-equation model coupled to optical propagation (transparent below threshold).
6. Lifetime response and pulse-sequence simulations.
7. Kerr/XPM phase-shift model and comparison with full-wave results.
8. Prompt-feature encoding, optical transfer, detector/readout, and digital decoding for a bounded end-to-end inference primitive; include encoder, detector noise, and calibration error.

## Baseline inputs

Use the Appendix A values from the source paper only as labeled baseline assumptions. Keep a separate file for measured updates, and never overwrite the baseline without recording a decision-log entry.

## Key modeling principles

1. **Directed scattering is computation, not loss.** Do not model node scattering as "insertion loss." The scattered field is the computational output. Only model absorbed or mode-mismatched light as loss.
2. **Propagation is an explicit parameter.** For the selected gas-filled hollow channel, model leakage and confinement from the measured final geometry; do not apply a solid-core TIR model or assume ~0.011 dB/cm.
3. **Path integral summation is the accumulation mechanism.** The output is the coherent sum of all directed scattered fields. Model the interference, not just power transmission.
4. **Separate the optical operation from language processing.** Model prompt tokenization/feature extraction, amplitude/phase encoding, the optical transfer, detection, and output decoding as explicit stages. Do not treat a laser wavefront alone as a text prompt or a complete language-model inference.
5. **Determine the binding constraint from measurements.** Propagation, mode conversion, bend loss, fabrication precision, and phase drift can each limit cascade depth.
6. **RSA zones are transparent below threshold.** Do not model RSA zones as lossy elements when below threshold.

## Required outputs

Each simulation run should produce configuration metadata, convergence evidence, parameter ranges, raw output, and a short interpretation stating whether the result is a demonstration, simulation, estimate, or hypothesis.
