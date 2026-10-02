# VOPU Architecture

## Computational model

VOPU is proposed as a hybrid optical/electronic inference system. A digital front end converts a prompt into numerical input features, an optical encoder maps those features onto a coherent laser field, and a fabricated 3D volume applies a fixed analog transformation through its channels, refractive-index landscape, and calibrated scattering nodes. The resulting fields combine by interference; detectors and a digital decoder turn the measured output into the next representation or output tokens. The volume does not directly read text or generate language by itself.

## Signal path

1. Train or select a bounded model/task and compile its supported numerical operation(s) into a fixed physical configuration: channel topology, node transfer functions, phase relationships, and material assignments.
2. Apply inverse shrinkage compensation to the fabrication geometry, then fabricate and calibrate the volume.
3. A digital prompt front end tokenizes text and forms the numerical vectors required by the selected model operation.
4. An optical encoder (for example, an SLM with coherent illumination) maps those vectors onto input-port amplitudes and phases. The prompt is represented by the launched field, not as literal text inside the substrate.
5. Face-coupled ports launch that field into the proposed 3D bus. Channels are continuous elongated ImpCarv cavities; they are liquid-filled during washing, and solvent exchange, ionic shrinkage, and supercritical-CO2 drying are intended to remove the liquid and leave gas-filled lumens. Hollow-mode confinement must be measured.
6. The encoded field interacts with the static refractive-index landscape and localized node structures. Dopant-mediated metallic reflective/scattering nodes are a fabrication hypothesis; their calibrated complex transfer functions would implement portions of the compiled weights.
7. Fields traveling along different paths acquire amplitude and phase changes and combine coherently. In the linear regime this is a physical linear transform; it is not, by itself, a complete transformer inference process.
8. Any required nonlinear/stateful operations must be provided by validated material responses, optical detection/feedback, or electronic stages. RSA, lifetime, and Q/K XPM are candidate mechanisms, not established functions.
9. Output detectors measure intensity and, where needed, phase using an appropriate coherent readout. Direct intensity detection alone does not recover arbitrary complex fields.
10. Calibration and digital decoding map detector measurements to the next numerical representation, logits, or output tokens. Autoregressive generation would require repeated encode-compute-readout cycles unless a validated optical recurrent implementation is provided.

## Prompt-to-output interface

The intended runtime path separates **prompt data**, **compiled analog weights**, and **decoded output**:

1. **Prompt to numbers:** software tokenizes the prompt and applies the chosen embedding/preprocessing model to obtain a numerical input vector or tensor. This conventional digital stage is part of the proposed system boundary.
2. **Numbers to optical field:** an encoder maps the numerical values to calibrated complex amplitudes across input ports or spatial modes. A coherent source and modulator set amplitude and phase; the launched wavefront carries the input. The optical carrier/interference pattern is not itself a text representation.
3. **Optical analog operation:** the fabricated configuration acts on the field. In a calibrated linear regime, write this as `E_out = T E_in`, where `T` is the measured transfer operator determined by the geometry and materials. Interference sums path contributions. Input-dependent nonlinear/stateful behavior requires separately validated mechanisms.
4. **Optical field to numbers:** detectors measure output intensity and/or phase. Coherent detection is needed when the downstream operation requires complex-field information; intensity-only measurements are not generally equivalent to complex-amplitude readout.
5. **Numbers to model output:** calibration software reconstructs numerical outputs, and a digital decoder interprets them as the next layer's input or token scores. A practical autoregressive language-model system would loop through these stages for successive tokens, with conventional digital processing wherever the physical volume does not implement a required operation.

The physical network is intended to store fixed weights; each prompt changes the input field, not the fabricated weight configuration. A claim of prompt inference must identify the supported task, encoder, compiled operation, detector/readout, decoder, and a numerical reference. The current project is a research program toward that interface, not a demonstrated prompt-to-text VOPU.

## Functional blocks

| Block | Intended function | Primary measurement |
|---|---|---|
| Prompt/feature encoder | Map numerical input features to calibrated optical amplitudes and phases | Encoding error, repeatability, and input-port calibration |
| Input coupler | Efficient field injection | Coupling efficiency and phase stability |
| 3D cavity channel | Route optical fields in the hollow lumen of elongated ImpCarv vacancies | Lumen cross-section/connectivity, hollow-mode confinement, propagation/bend loss |
| Reflective node | Dopant-mediated metal feature with designed reflective orientation | Conversion chemistry, facet geometry, reflectance, absorption, angular scattering |
| RSA zone | Intensity thresholding (transparent below threshold) | Transmission versus intensity and recovery |
| Lifetime zone | Short-term memory | Impulse response and decay constant |
| XPM zone | Dynamic Q/K interaction | Differential phase versus powers and overlap |
| Output detector/readout | Measure output intensity and, when required, complex field | SNR, dynamic range, phase-retrieval error |
| Digital output decoder | Convert measured features to next-layer values or token scores | Numerical-reference error and repeatability |

## Weight and state mapping

### Frozen volumetric weights

For a selected supported operation, trained model parameters are compiled into a fixed physical configuration. Weight tensors are proposed to be represented by combinations of:

- waveguide topology and path selection;
- refractive-index landscape and local index contrast;
- terminal-node directed scattering patterns;
- phase shifts and coupling strengths; and
- node geometry and incidence/coupling angle.

The fabricated volume is intended as a static physical weight store. Runtime input data are encoded onto light; optical scattering and path-integral interference apply the calibrated operation. Digital encoding, readout, and decoding remain part of the system.

### Passive state adaptivity

The static weight configuration is supplemented by material state:

- **Epsilon-thresholding:** reverse-saturable-absorber zones are transparent below threshold and absorb above it, suppressing sub-threshold activations and transmitting sufficiently strong fields.
- **Lambda-decay:** excited chromophore states temporarily change refractive index and absorption, then relax with characteristic lifetime `tau`, giving sequential pulses temporal context.
- **Dynamic Q/K interaction:** overlapping query and key fields modulate refractive paths through cross-phase modulation, supplying a physical operand interaction.

These mechanisms are proposed device functions and require independent characterization before system-level claims.

## Compiler and fabrication workflow

1. Select a measurable model operation and extract its numerical weights and input/output conventions.
2. Synthesize the 3D interconnect topology and terminal-node locations for that operation.
3. Apply inverse shrinkage compensation.
4. Prepare the hydrogel precursor and measure its refractive index.
5. Two-photon pattern elongated routing cavities. Develop and wash while they are liquid-filled; maintain accessible channel openings for washing and solvent exchange.
6. Apply formulation-specific ionic dehydration/shrinkage, solvent exchange, and supercritical-CO2 drying; verify liquid removal and lumen survival. Test dopant-mediated reflective-node chemistry and its compatibility with these steps separately before integration.
7. Measure the post-process geometry and optical response, calibrate the input encoder, device transfer, detector, and readout, then package the sample in an aligned optical housing.
8. Tokenize a test prompt, encode its selected numerical representation into the calibrated optical input, run a bounded operation, and compare detector-derived outputs with the compiled numerical reference before attempting language-model decoding.

## Reference parameters

The source architecture uses a 532 nm baseline wavelength, approximately 1.48 substrate index, approximately 0.40 peak index contrast, and a 1.2 ns nominal relaxation lifetime. These remain provisional inputs, not accepted specifications. The solid-core index/contrast parameters do not specify the selected hollow-core channel; model its boundary geometry and measure mode confinement and loss after shrinkage and drying. Record provenance and evidence status in the claim register.

## Critical interfaces

- Geometry-to-scattering transfer: shrinkage must map written geometry to the intended post-shrinkage scattering pattern.
- Material-to-response transfer: dopant concentration and local chemistry must map to measured absorption, lifetime, and nonlinear coefficients.
- Scattering-to-computation transfer: calibration must map measured scattered fields to numerical tensor operations via path integral reconstruction.
- Compiler-to-geometry transfer: the inverse-shrinkage-compensated design must survive fabrication without changing the compiled operation.
- Fabrication-to-economics transfer: yield and write throughput must be measured rather than inferred from idealized process conditions.
