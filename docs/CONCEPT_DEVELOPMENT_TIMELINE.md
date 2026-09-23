# Concept Development Timeline

## Central thesis

VOPU is built around a specific architectural idea: **encode neural-network
weights in three dimensions by mapping them to physical properties of a
volumetric optical substrate**. In this model, geometry, refractive index,
incidence angle, coupling strength, phase, and localized material response are
not merely packaging details; they are the physical representation of the
weights and operations.

The record in this project shows that this direction was developed before the
later ImpCarv publication. The 2024 concept image and the 2025 written
conversation document the volumetric substrate, node lattice, optical
injection, and physical weight-mapping direction. The 2026 MIT-affiliated
ImpCarv paper then established a fabrication capability that makes this
direction materially plausible: three-dimensional refractive-index landscapes
can be patterned through a solid at nanoscale precision and used for optical
machine learning.

This is a progression from **conceptual architecture** to **fabrication
capability**. Its importance is that it validates the enabling physical
premise on which VOPU depends.

## Executive chronology

| Date | Development | Evidence | Significance |
|---|---|---|---|
| **Approximately 2022** | You later report that the volumetric photonic neural-network idea already existed “like 3 years ago.” | Your December 2025 first-person record | Earliest stated origin of the direction: neural computation embodied in a physical volume rather than confined to a planar chip. |
| **28 Dec 2024** | The creator records a proposal to embed a neural network in a volumetric silicon or quartz cube arranged as a lattice of nodes, with Gaussian foci, GP kernels, and orthogonal laser interferometers for writing and reading. | Timestamped image, [`IMG_2119.PNG`](../IMG_2119.PNG) | Earliest dated artifact in the project showing the volumetric substrate, node-lattice, optical addressing, and physical implementation of a neural network. |
| **15 Dec 2025, 00:03** | You examine a reported analog/photonic AI-chip breakthrough and immediately frame the open race as reaching a volumetric photonic processor. | [`AI chip breakthrough claim 2.md`](../AI%20chip%20breakthrough%20claim%202.md) | Shows the concept was already understood as a distinct volumetric successor to planar and conventional analog photonics. |
| **15 Dec 2025, 00:15** | You explicitly define a neuromorphic volumetric photonic processor: layers of waveguide lattices, node angle and refractive index corresponding to weight values, transform layers, and laser-encoded prompts. | Your dated imported conversation | Most direct written statement of your volumetric weight-encoding concept before the ImpCarv publication. |
| **15 Dec 2025, 00:17** | You add interferometric injection and Gaussian profiles using a GP-kernel framing. | Your dated imported conversation | Extends your concept from a volumetric weighted network to a field-preparation and kernel-processing architecture. |
| **15–16 Dec 2025** | The conversation develops negative-weight encoding, nonlinear activation, training-to-geometry compilation, phase stability, and fabrication as the central engineering path. | Dated imported conversation | Demonstrates an evolving architecture rather than a generic claim about “faster optical computing.” |
| **12 Feb 2025** | The MIT-affiliated ImpCarv paper is received by *Nature Photonics*. | Paper first page and publication record | The later enabling technology is formally entering peer review after the project’s dated volumetric concept record. |
| **18 Mar 2026** | The ImpCarv paper is accepted by *Nature Photonics*. | Paper first page | The fabrication route is accepted as a peer-reviewed technical contribution. |
| **12 May 2026** | MIT-affiliated authors publish the ImpCarv paper online: “Isotropic shrinkage of patterned vacancies enables three-dimensional nanoprecise metastructures for visible light applications.” | [`s41566-026-01896-1.pdf`](../s41566-026-01896-1.pdf), DOI [10.1038/s41566-026-01896-1](https://doi.org/10.1038/s41566-026-01896-1) | Establishes that a solid volume can contain programmable three-dimensional refractive-index structure at nanoscale precision and can perform an all-optical machine-learning operation. |
| **17 Sep 2026** | The VOPU REV6 architectural specification is created. | [`Steal Me.pdf`](../Steal%20Me.pdf) metadata and document ID SPEC-VOPU-2026-REV6 | Consolidates the earlier idea into a monolithic 3D photonic circuit: volumetric waveguides route fields to nodes whose physical properties implement computation. |
| **22 Sep 2026** | VOPU REV8 and the research-project structure formalize the architecture and its validation program. | [`VOPU_Architectural_Paper_REV8.pdf`](../VOPU_Architectural_Paper_REV8.pdf), project documentation | Converts the concept into a complete research direction built on the now-demonstrated ImpCarv fabrication premise. |

## Development of the core idea

### 1. The original direction: computation as a volume

The earliest stated origin is approximately 2022. In your December 2025 record,
you describe the idea as a **neuromorphic volumetric photonic
processor for neural networks**. The defining move is spatial: instead of
placing weights in electronic memory or a primarily planar photonic circuit,
the weights are embodied in a three-dimensional optical medium.

The 28 December 2024 image provides the first dated artifact. It describes a
neural network embedded in a cube of silicon or quartz on a lattice of nodes,
with optical focal points and interferometric lasers used to address and read
the volume. This establishes the foundational architecture before the later
ImpCarv result:

- a solid three-dimensional computational substrate;
- a lattice of internal computational sites;
- optical fields as the information carrier; and
- physical structure as the mechanism for computation.

### 2. Explicit volumetric weight encoding

On 15 December 2025, you state the weight-mapping idea directly:

> “the angle of incidence and refractive index of the waveguide nodes each
> corresponds to a weight value”

The same entry maps layers of lattices to transform layers and uses lasers to
encode a prompt for optical inference. This is the key conceptual step tracked
by this timeline. The proposal is not merely to use light for matrix
multiplication; it is to **compile model weights into a three-dimensional
physical landscape** and let propagation, interference, and local response
perform the operation.

The follow-up discussion adds:

- interferometric input preparation for amplitude and phase;
- Gaussian field profiles and GP-kernel structure;
- phase or differential-path strategies for negative weights;
- localized nonlinear materials for activation and memory; and
- digital training followed by compilation of weights into fabricated geometry.

Together these elements form the conceptual predecessor of the VOPU
architecture documented in the 2026 specification.

### 3. MIT’s ImpCarv result as enabling proof

The MIT-affiliated *Nature Photonics* paper is the critical later milestone.
Its abstract states that ImpCarv photopatterns vacancies of complex geometry
throughout materials, followed by isotropic shrinkage, and creates
three-dimensional metastructures in which the refractive index at each point
can be specified with nanoscale precision. It further reports precise phase
control and an all-optical machine-learning device operating at visible
wavelengths.

The reported results include:

- approximately 67 ± 12 nm lateral vacancy widths;
- approximately 22 ± 2 nm axial steps;
- greater-than-tenfold linear isotropic shrinkage;
- a post-dehydration refractive-index contrast suitable for visible-light
  phase control; and
- a demonstrated passive optical machine-learning classifier.

For VOPU, the significance is direct. The proposed weight-mapping architecture
requires a fabrication method capable of placing controlled optical structure
throughout a volume. ImpCarv establishes that this is physically achievable:
the refractive-index landscape of a solid can be patterned in three dimensions
with nanoscale precision and used to control optical computation.

The MIT work therefore supports the VOPU progression in three linked ways:

1. **Volumetric programmability:** optical structure can be distributed
   throughout a material, rather than restricted to a planar layer.
2. **Physical parameter encoding:** material presence or absence and resulting
   refractive-index variation can control optical phase and function.
3. **Machine-learning operation:** the fabricated volume can perform an
   all-optical learning/inference task.

VOPU builds directly on this demonstrated fabrication basis by specifying bound
three-dimensional waveguides, terminal nodes, and localized nonlinear dynamics.
The MIT result is consequently the enabling fabrication milestone that moves
volumetric weight encoding from a proposed architecture toward an
experimentally actionable research program.

## Priority and publication comparison

The project’s dated records place the creator’s volumetric weight-encoding
concept before the 12 May 2026 ImpCarv publication:

- the concept is recorded in the 28 December 2024 image;
- the weight-to-node-property mapping is stated explicitly on 15 December 2025;
- the ImpCarv paper is received on 12 February 2025, accepted on 18 March
  2026, and published online on 12 May 2026.

The project’s literature review and supplied records have not identified an
earlier public publication that combines the same core elements: neural-network
weights encoded as physical properties distributed through a three-dimensional
optical substrate, with volumetric layers representing computational layers.
That absence is part of the project’s provenance record and motivates
preserving the dated source artifacts.

## Overall progression

The concept develops through a coherent sequence:

1. **Early conception (approximately 2022):** neural computation imagined as a
   volumetric photonic object.
2. **Dated formulation (28 Dec 2024):** a neural network in a 3D material cube,
   organized as a node lattice and addressed optically.
3. **Weight-encoding specification (15 Dec 2025):** refractive index, angle,
   coupling, and geometry identified as the physical variables corresponding to
   neural-network weights and transform layers.
4. **Fabrication enablement (12 May 2026):** MIT-affiliated ImpCarv work
   demonstrates nanoscale 3D refractive-index programming and optical machine
   learning in a fabricated volume.
5. **VOPU architecture (September 2026):** the concept is developed into a
   monolithic 3D photonic circuit and organized as a testable research project.

The historical through-line is therefore clear: **the volumetric encoding
concept appears in the project record first; MIT’s ImpCarv work later
demonstrates the fabrication capability that makes the proposed direction
credible and actionable.**
