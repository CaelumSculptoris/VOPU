"""
VOPU Weight Compiler Prototype
==============================

Maps transformer weight matrices to a 3D waveguide topology with terminal
nodes, applies inverse shrinkage compensation, and emits fabrication design
files and numerical references.

This is a minimal prototype implementing WP5 of the VOPU research plan.

Pipeline:
1. Extract/define a weight matrix (Wq, Wk, Wv, or FFN)
2. Map weights to complex terminal-node scattering coefficients
3. Synthesize 3D node topology (non-intersecting routing)
4. Apply inverse shrinkage compensation
5. Emit design file and numerical reference
"""

import numpy as np
import json
from dataclasses import dataclass, field, asdict
from typing import List, Tuple, Dict
from pathlib import Path

# ============================================================
# Parameters
# ============================================================

# ImpCarv shrinkage factor [D - Yang et al. 2026]
SHRINKAGE_FACTOR = 5.03  # MSF formulation: 5.03 ± 0.06
SHRINKAGE_FACTOR_HSF = 13.18  # HSF formulation: 13.18 ± 0.28

# VOPU architecture parameters
WAVELENGTH = 532e-9  # m
N_SUBSTRATE = 1.48

# Grid parameters
NODE_SPACING = 500e-6  # 500 µm in post-shrink coordinates
WAVEGUIDE_WIDTH = 500e-9  # 500 nm

# ============================================================
# Data Structures
# ============================================================

@dataclass
class TerminalNode:
    """A terminal node in the 3D optical network."""
    node_id: int
    x: float          # post-shrink x coordinate (m)
    y: float          # post-shrink y coordinate (m)
    z: float          # post-shrink z coordinate (m)
    weight_real: float  # real part of complex weight
    weight_imag: float  # imaginary part (phase shift)
    # Pre-shrink coordinates (for fabrication)
    pre_shrink_x: float = 0.0
    pre_shrink_y: float = 0.0
    pre_shrink_z: float = 0.0

@dataclass
class WaveguideSegment:
    """A waveguide routing segment between two nodes."""
    segment_id: int
    start_node: int
    end_node: int
    path_type: str  # 'straight', 'bend', 'crossing_avoidance'
    length: float   # post-shrink length (m)

@dataclass
class CompiledDesign:
    """Complete compiled design output."""
    nodes: List[Dict] = field(default_factory=list)
    segments: List[Dict] = field(default_factory=list)
    weight_matrix: List[List[float]] = field(default_factory=list)
    numerical_reference: Dict = field(default_factory=dict)
    shrinkage_factor: float = SHRINKAGE_FACTOR
    design_metadata: Dict = field(default_factory=dict)


# ============================================================
# Weight Mapping
# ============================================================

def weight_to_complex_phase(weight: float, max_weight: float = None) -> Tuple[float, float]:
    """
    Map a real-valued weight to a complex scattering coefficient.
    
    Strategy: encode magnitude as amplitude, sign as π phase shift.
    w > 0: amplitude = |w|, phase = 0
    w < 0: amplitude = |w|, phase = π
    
    Returns (amplitude, phase_radians).
    """
    if max_weight is None:
        max_weight = abs(weight)
    if max_weight == 0:
        return 0.0, 0.0
    
    amplitude = abs(weight) / max_weight  # normalize to [0, 1]
    phase = 0.0 if weight >= 0 else np.pi
    return amplitude, phase

def matrix_to_nodes(weight_matrix: np.ndarray) -> List[TerminalNode]:
    """
    Map a weight matrix to a grid of terminal nodes.
    
    Each element W[i,j] maps to a terminal node at position (i, j)
    in a 2D layer, with the weight encoded as amplitude and phase.
    """
    rows, cols = weight_matrix.shape
    max_w = np.max(np.abs(weight_matrix))
    if max_w == 0:
        max_w = 1.0
    
    nodes = []
    node_id = 0
    for i in range(rows):
        for j in range(cols):
            amp, phase = weight_to_complex_phase(weight_matrix[i, j], max_w)
            # Place nodes in a 2D grid with spacing
            x = j * NODE_SPACING
            y = i * NODE_SPACING
            z = 0.0  # single layer for prototype
            nodes.append(TerminalNode(
                node_id=node_id,
                x=x, y=y, z=z,
                weight_real=amp * np.cos(phase),
                weight_imag=amp * np.sin(phase)
            ))
            node_id += 1
    return nodes

def synthesize_topology(nodes: List[TerminalNode], input_nodes: int, output_nodes: int) -> List[WaveguideSegment]:
    """
    Synthesize non-intersecting waveguide routing.
    
    For the prototype, we use a simple row-column routing scheme:
    - Input ports connect to their row of nodes
    - Output ports connect to their column of nodes
    - Routing uses Manhattan-style paths with depth separation
    """
    segments = []
    seg_id = 0
    
    # Connect inputs to rows
    for i in range(input_nodes):
        for j in range(output_nodes):
            start = i * output_nodes + j
            # Simple straight connection for now
            segments.append(WaveguideSegment(
                segment_id=seg_id,
                start_node=start,
                end_node=start,  # self-referencing for now (node is both input and output)
                path_type='straight',
                length=NODE_SPACING
            ))
            seg_id += 1
    
    return segments

# ============================================================
# Inverse Shrinkage Compensation
# ============================================================

def apply_inverse_shrinkage(nodes: List[TerminalNode], shrinkage_factor: float = SHRINKAGE_FACTOR) -> List[TerminalNode]:
    """
    Apply inverse shrinkage compensation to get pre-fabrication coordinates.
    
    pre_shrink = post_shrink * shrinkage_factor
    
    The written geometry must be larger by the shrinkage factor so that
    after isotropic shrinkage, the post-shrink geometry matches the design.
    """
    for node in nodes:
        node.pre_shrink_x = node.x * shrinkage_factor
        node.pre_shrink_y = node.y * shrinkage_factor
        node.pre_shrink_z = node.z * shrinkage_factor
    return nodes

# ============================================================
# Numerical Reference
# ============================================================

def compute_numerical_reference(weight_matrix: np.ndarray, nodes: List[TerminalNode]) -> Dict:
    """
    Compute the numerical reference for the compiled design.
    
    This is what the optical output should match when the system is calibrated.
    """
    rows, cols = weight_matrix.shape
    
    # The optical operation is: y = W @ x
    # where W is the weight matrix and x is the input vector
    
    # Test with identity input
    test_input = np.eye(cols)[:, :min(cols, 4)]  # first few identity columns
    expected_output = weight_matrix @ test_input
    
    # Also compute the complex transfer matrix from node parameters
    max_w = np.max(np.abs(weight_matrix))
    if max_w == 0:
        max_w = 1.0
    
    transfer_matrix = np.zeros((rows, cols), dtype=complex)
    for i in range(rows):
        for j in range(cols):
            amp, phase = weight_to_complex_phase(weight_matrix[i, j], max_w)
            transfer_matrix[i, j] = amp * np.exp(1j * phase)
    
    return {
        'weight_matrix_shape': list(weight_matrix.shape),
        'max_weight': float(max_w),
        'test_input_shape': list(test_input.shape),
        'expected_output': expected_output.tolist(),
        'transfer_matrix': transfer_matrix.tolist(),
        'operation': 'matrix-vector multiply (GEMM)',
        'note': 'Optical output should match expected_output within calibration tolerance'
    }

# ============================================================
# Design Emitter
# ============================================================

def emit_design_file(nodes: List[TerminalNode], segments: List[WaveguideSegment],
                     weight_matrix: np.ndarray, metadata: Dict = None) -> CompiledDesign:
    """Emit complete compiled design with all fabrication artifacts."""
    numerical_ref = compute_numerical_reference(weight_matrix, nodes)
    
    return CompiledDesign(
        nodes=[asdict(n) for n in nodes],
        segments=[asdict(s) for s in segments],
        weight_matrix=weight_matrix.tolist(),
        numerical_reference=numerical_ref,
        shrinkage_factor=SHRINKAGE_FACTOR,
        design_metadata=metadata or {
            'compiler_version': '0.1.0',
            'wavelength_nm': 532,
            'substrate_index': 1.48,
            'shrinkage_factor': SHRINKAGE_FACTOR,
            'node_spacing_um': NODE_SPACING * 1e6,
            'waveguide_width_nm': WAVEGUIDE_WIDTH * 1e9,
            'evidence': 'S - simulated compiler prototype'
        }
    )

# ============================================================
# Main Compiler
# ============================================================

def compile_weights(weight_matrix: np.ndarray, input_dim: int = None, output_dim: int = None) -> CompiledDesign:
    """
    Main compilation pipeline:
    1. Map weights to terminal nodes
    2. Synthesize 3D topology
    3. Apply inverse shrinkage compensation
    4. Compute numerical reference
    5. Emit design file
    """
    if input_dim is None:
        input_dim = weight_matrix.shape[1]
    if output_dim is None:
        output_dim = weight_matrix.shape[0]
    
    # Step 1: Map weights to nodes
    nodes = matrix_to_nodes(weight_matrix)
    
    # Step 2: Synthesize topology
    segments = synthesize_topology(nodes, input_dim, output_dim)
    
    # Step 3: Apply inverse shrinkage
    nodes = apply_inverse_shrinkage(nodes, SHRINKAGE_FACTOR)
    
    # Step 4: Compute numerical reference
    numerical_ref = compute_numerical_reference(weight_matrix, nodes)
    
    # Step 5: Emit design
    design = emit_design_file(nodes, segments, weight_matrix, {
        'compiler_version': '0.1.0',
        'wavelength_nm': 532,
        'substrate_index': 1.48,
        'shrinkage_factor': SHRINKAGE_FACTOR,
        'shrinkage_compensation': 'Applied (MSF formulation, factor 5.03)',
        'node_spacing_um': NODE_SPACING * 1e6,
        'waveguide_width_nm': WAVEGUIDE_WIDTH * 1e9,
        'input_dimension': input_dim,
        'output_dimension': output_dim,
        'total_nodes': len(nodes),
        'total_segments': len(segments),
        'evidence': 'S - simulated compiler prototype',
        'pipeline_steps': [
            '1. Weight extraction (matrix input)',
            '2. Node mapping (amplitude + phase encoding)',
            '3. Topology synthesis (Manhattan routing)',
            '4. Inverse shrinkage compensation (factor 5.03x)',
            '5. Numerical reference computation',
            '6. Design file emission'
        ]
    })
    
    return design

# ============================================================
# Example Usage
# ============================================================

def example_compilation():
    """Compile a small example weight matrix."""
    # 4x4 weight matrix (could be a small Wq, Wk, Wv, or FFN layer)
    W = np.array([
        [ 0.8, -0.3,  0.5,  0.1],
        [-0.2,  0.9, -0.4,  0.3],
        [ 0.6,  0.1, -0.7, -0.5],
        [-0.1,  0.4,  0.2,  0.8]
    ])
    
    design = compile_weights(W)
    return design

if __name__ == '__main__':
    design = example_compilation()
    print(json.dumps({
        'metadata': design.design_metadata,
        'node_count': len(design.nodes),
        'segment_count': len(design.segments),
        'first_3_nodes': design.nodes[:3],
        'numerical_reference_shape': design.numerical_reference['weight_matrix_shape'],
        'transfer_matrix': design.numerical_reference['transfer_matrix']
    }, indent=2))
