"""
Phase Error Budget for VOPU Cascaded Network
=============================================

Computes phase error accumulation across cascaded terminal nodes and
determines fabrication tolerance requirements.

Phase errors are separated into two categories:
1. NODE-SPECIFIC errors: variation in the complex weight applied by each node
   (fabrication tolerance of node geometry, local index variation, node scattering)
   These accumulate as sqrt(N) across N nodes.
2. PATH-SPECIFIC errors: systematic phase drift along propagation paths
   (thermal drift, long-path index variation)
   These are calibratable and do not accumulate in the same way.

The cascability-relevant error is the node-specific per-node phase error,
which determines how much the actual weight matrix deviates from the
intended one.

Reference parameters:
  - Wavelength: 532 nm
  - ImpCarv lateral tolerance: ±12 nm [D]
  - ImpCarv axial tolerance: ±2 nm [D]
  - Thermal coefficient: ~10^-4 /K (polymer) [E]
  - Node size: ~500 nm (post-shrink)
  - Node spacing: ~500 µm
"""

import numpy as np
import json

WAVELENGTH = 532e-9  # meters
PI = np.pi

# ImpCarv fabrication tolerance [D - Yang et al. 2026]
LAT_TOLERANCE = 12e-9   # ±12 nm lateral [D]
AX_TOLERANCE = 2e-9     # ±2 nm axial [D]

# Thermal parameters [E - typical polymer/hydrogel]
DN_DT = 1e-4             # dn/dT for polymer (~10^-4 /K) [E]
DL_DT = 5e-5             # dL/dT thermal expansion (~5×10^-5 /K) [E]

# VOPU architecture parameters
N_SUBSTRATE = 1.48
DELTA_N = 0.40
N_CORE = N_SUBSTRATE + DELTA_N  # 1.88
N_CLAD = N_SUBSTRATE              # 1.48
N_EFF = (N_CORE + N_CLAD) / 2     # ~1.68

# Geometry
NODE_SIZE = 500e-9        # node dimension (post-shrink) [E]
NODE_SPACING = 500e-6    # inter-node spacing [E]

def phase_error_fabrication(tolerance, n_eff, wavelength):
    """Phase error from dimensional tolerance at a node."""
    return (2 * PI / wavelength) * n_eff * tolerance

def phase_error_index_node(delta_n, node_size, wavelength):
    """Phase error from local refractive index variation at a node."""
    return (2 * PI / wavelength) * delta_n * node_size

def phase_error_thermal_node(delta_T, n_eff, node_size, wavelength):
    """Phase error from thermal drift at a node (node-scale, not path-scale)."""
    return (2 * PI / wavelength) * (DN_DT * delta_T * node_size + n_eff * DL_DT * delta_T * node_size)

def phase_error_thermal_path(delta_T, n_eff, path_length, wavelength):
    """
    Phase error from thermal drift along inter-node path.
    This is a SYSTEMATIC error that can be calibrated; reported separately.
    """
    return (2 * PI / wavelength) * (DN_DT * delta_T * path_length + n_eff * DL_DT * delta_T * path_length)

def accumulate_phase_errors(n_nodes, sigma_per_node):
    """Accumulate uncorrelated phase errors: σ_total = σ_per_node * sqrt(N)."""
    return sigma_per_node * np.sqrt(n_nodes)

def run_phase_budget():
    results = {}
    
    # --- Per-NODE phase errors (cascability-relevant) ---
    # 1. Fabrication: lateral and axial tolerance at node scale
    sigma_fab_lateral = phase_error_fabrication(LAT_TOLERANCE, N_EFF, WAVELENGTH)
    sigma_fab_axial = phase_error_fabrication(AX_TOLERANCE, N_EFF, WAVELENGTH)
    sigma_fab = np.sqrt(sigma_fab_lateral**2 + sigma_fab_axial**2)
    
    # 2. Thermal drift at node (±0.5 K)
    delta_T = 0.5  # K
    sigma_thermal_node = phase_error_thermal_node(delta_T, N_EFF, NODE_SIZE, WAVELENGTH)
    
    # 3. Index variation at node (±1% of Δn = 0.004)
    delta_n_var = 0.01 * DELTA_N  # 0.004
    sigma_index_node = phase_error_index_node(delta_n_var, NODE_SIZE, WAVELENGTH)
    
    # 4. Node scattering variation (±5% of π phase per node)
    sigma_node_scatter = 0.05 * PI  # ~0.157 rad per node
    
    # Total per-node sigma (uncorrelated)
    sigma_per_node = np.sqrt(sigma_fab**2 + sigma_thermal_node**2 + sigma_index_node**2 + sigma_node_scatter**2)
    
    results['per_node_errors'] = {
        'fabrication_lateral_rad': float(sigma_fab_lateral),
        'fabrication_lateral_deg': float(np.degrees(sigma_fab_lateral)),
        'fabrication_axial_rad': float(sigma_fab_axial),
        'fabrication_axial_deg': float(np.degrees(sigma_fab_axial)),
        'fabrication_total_rad': float(sigma_fab),
        'fabrication_total_deg': float(np.degrees(sigma_fab)),
        'thermal_node_0.5K_rad': float(sigma_thermal_node),
        'thermal_node_0.5K_deg': float(np.degrees(sigma_thermal_node)),
        'index_variation_rad': float(sigma_index_node),
        'index_variation_deg': float(np.degrees(sigma_index_node)),
        'node_scatter_rad': float(sigma_node_scatter),
        'node_scatter_deg': float(np.degrees(sigma_node_scatter)),
        'total_per_node_rad': float(sigma_per_node),
        'total_per_node_deg': float(np.degrees(sigma_per_node)),
        'evidence': 'S - simulated; fabrication tolerance from [D] Yang et al. 2026; node-scale errors'
    }
    
    # --- PATH-SPECIFIC systematic errors (calibratable, reported separately) ---
    sigma_thermal_path = phase_error_thermal_path(delta_T, N_EFF, NODE_SPACING, WAVELENGTH)
    
    results['path_systematic_errors'] = {
        'thermal_path_0.5K_rad': float(sigma_thermal_path),
        'thermal_path_0.5K_deg': float(np.degrees(sigma_thermal_path)),
        'note': 'These are systematic phase shifts along inter-node paths. They can be measured '
                'and calibrated during system initialization. They do NOT accumulate as sqrt(N) '
                'but rather create a fixed phase offset pattern that can be compensated.',
        'calibration_requirement': f'Thermal path drift of {np.degrees(sigma_thermal_path):.1f}° per 0.5K requires '
                                    f'active thermal stabilization or per-path phase calibration.',
        'evidence': 'E - first-order estimate'
    }
    
    # --- Cascaded phase error (node-specific only) ---
    node_range = np.arange(1, 201)
    sigma_cascaded = accumulate_phase_errors(node_range, sigma_per_node)
    
    # Phase error tolerances
    PHASE_TOLERANCE_45 = PI / 4       # 45 degrees
    PHASE_TOLERANCE_225 = PI / 8     # 22.5 degrees
    PHASE_TOLERANCE_10 = PI / 18     # 10 degrees (strict)
    
    max_depth_45 = (PHASE_TOLERANCE_45 / sigma_per_node) ** 2
    max_depth_225 = (PHASE_TOLERANCE_225 / sigma_per_node) ** 2
    max_depth_10 = (PHASE_TOLERANCE_10 / sigma_per_node) ** 2
    
    results['cascaded'] = {
        'depths': node_range.tolist(),
        'sigma_total_rad': sigma_cascaded.tolist(),
        'sigma_total_degrees': np.degrees(sigma_cascaded).tolist(),
        'phase_tolerance_45deg_rad': PHASE_TOLERANCE_45,
        'phase_tolerance_45deg_deg': float(np.degrees(PHASE_TOLERANCE_45)),
        'phase_tolerance_22.5deg_rad': PHASE_TOLERANCE_225,
        'phase_tolerance_22.5deg_deg': float(np.degrees(PHASE_TOLERANCE_225)),
        'phase_tolerance_10deg_rad': PHASE_TOLERANCE_10,
        'phase_tolerance_10deg_deg': float(np.degrees(PHASE_TOLERANCE_10)),
        'max_depth_45deg': float(max_depth_45),
        'max_depth_22.5deg': float(max_depth_225),
        'max_depth_10deg': float(max_depth_10),
        'evidence': 'S - simulated from uncorrelated node-scale error accumulation'
    }
    
    # --- Breakdown at key depths ---
    depth_breakdown = []
    for depth in [1, 5, 10, 20, 50, 100, 200]:
        sigma = sigma_per_node * np.sqrt(depth)
        depth_breakdown.append({
            'depth': depth,
            'sigma_rad': float(sigma),
            'sigma_deg': float(np.degrees(sigma)),
            'within_45deg': bool(sigma < PHASE_TOLERANCE_45),
            'within_22.5deg': bool(sigma < PHASE_TOLERANCE_225),
            'within_10deg': bool(sigma < PHASE_TOLERANCE_10)
        })
    results['depth_breakdown'] = depth_breakdown
    
    # --- Dominant error source ---
    errors = {
        'fabrication': sigma_fab,
        'thermal_node': sigma_thermal_node,
        'index_variation': sigma_index_node,
        'node_scatter': sigma_node_scatter
    }
    dominant = max(errors, key=errors.get)
    
    results['findings'] = {
        'dominant_error_source': dominant,
        'dominant_error_rad': float(errors[dominant]),
        'dominant_error_deg': float(np.degrees(errors[dominant])),
        'dominant_error_fraction': float(errors[dominant] / sigma_per_node),
        'total_per_node_deg': float(np.degrees(sigma_per_node)),
        'max_depth_45deg': float(max_depth_45),
        'max_depth_22.5deg': float(max_depth_225),
        'max_depth_10deg': float(max_depth_10),
        'path_thermal_drift_deg': float(np.degrees(sigma_thermal_path)),
        'implication': (
            f"The dominant per-node phase error is '{dominant}' "
            f"({errors[dominant]/sigma_per_node*100:.0f}% of total, {np.degrees(errors[dominant]):.1f}°). "
            f"Total per-node error is {np.degrees(sigma_per_node):.1f}° (1σ). "
            f"Maximum cascade depth: {max_depth_45:.0f} nodes (45° tol), "
            f"{max_depth_225:.0f} nodes (22.5° tol), {max_depth_10:.0f} nodes (10° tol). "
            f"Inter-node path thermal drift is {np.degrees(sigma_thermal_path):.1f}° per 0.5K "
            f"but is calibratable. Fabrication tolerance and node scattering variation "
            f"are the primary targets for improvement."
        ),
        'evidence': 'S - simulated from first-order phase budget with node-scale errors'
    }
    
    return results

if __name__ == '__main__':
    results = run_phase_budget()
    print(json.dumps(results, indent=2))
