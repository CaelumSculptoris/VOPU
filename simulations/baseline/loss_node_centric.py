"""
VOPU Node-Centric Loss Model — Directed Scattering is Computation
==================================================================

Fundamental reframing: terminal nodes are COMPUTING elements, not loss
elements. The directed scattering at each node IS the weight multiplication.
The path integral summation of scattered fields IS the accumulation.

What I was calling "node insertion loss" is the computation itself. The only
real loss is the UNDESIRED fraction — light that scatters into wrong modes,
gets absorbed by node material, or reflects backward.

Loss budget should be:
1. Coupling loss (input/output facets)
2. Undesired scattering at nodes (efficiency shortfall, NOT the directed field)
3. Material absorption (if nodes have absorbing materials like RSA zones)
4. Propagation (negligible — fiber-like)
5. Bend radiation (small for high-NA guides)

The "insertion loss" concept from passive photonics doesn't apply here.
In passive photonics, a node redirects light and you lose some. In VOPU,
the node IS the operation — the redirected light is the answer.
"""

import numpy as np
import json

# ============================================================
# Corrected Model Parameters
# ============================================================

# Propagation: fiber-like, negligible [D - fiber principle]
WG_PROPAGATION_LOSS = 0.011  # dB/cm (includes roughness)

# Node scattering efficiency
# A well-designed directed scattering node sends most light to the target.
# The "loss" is only the fraction that goes elsewhere.
NODE_SCATTERING_EFFICIENCY = 0.95   # 95% of light goes where directed [E - target]
NODE_UNDESIRED_LOSS_DB = -10 * np.log10(NODE_SCATTERING_EFFICIENCY)  # 0.22 dB undesired

# But even "undesired" scattered light contributes to the path integral!
# Only truly absorbed or mode-mismatched light is lost.
NODE_ABSORPTION_FRACTION = 0.02     # 2% absorbed by node material [E]
NODE_ABSORPTION_LOSS_DB = -10 * np.log10(1 - NODE_ABSORPTION_FRACTION)  # 0.09 dB

# True node loss = absorption only (directed scattering is computation)
NODE_TRUE_LOSS = NODE_ABSORPTION_LOSS_DB  # 0.09 dB — absorption, not scattering

# RSA zones DO absorb (that's their function — epsilon-thresholding)
# But RSA absorption is the nonlinearity, not loss. It only activates
# above threshold. Below threshold, RSA zones are transparent.
RSA_TRANSPARENT_LOSS_DB = 0.001  # negligible when below threshold [E]

# Coupling
COUPLING_LOSS = 0.5  # dB per facet [E]
COUPLING_OPTIMIZED = 0.2  # dB per facet with mode matching [E]

# Bend loss (radiation at corners)
BEND_LOSS_PER_TURN = 0.005  # dB per 90° bend (high-NA guide) [E]

# System
LASER_POWER_DBM = 10
NOISE_FLOOR_DBM = -70
REQUIRED_SNR_DB = 15
PATH_PER_NODE_CM = 0.1
BENDS_PER_NODE = 0.5

# ============================================================
# Analysis
# ============================================================

def compute_budget(n_nodes, node_loss, coupling_loss, wg_loss=WG_PROPAGATION_LOSS):
    """
    Compute loss budget for n-node network.

    Total loss = coupling + n * (node_absorption + propagation + bends)
    Note: directed scattering is NOT included — it's computation.
    """
    prop = n_nodes * wg_loss * PATH_PER_NODE_CM
    nodes = n_nodes * node_loss
    bends = n_nodes * BENDS_PER_NODE * BEND_LOSS_PER_TURN
    coup = coupling_loss
    total = coup + nodes + prop + bends
    return {
        'n_nodes': n_nodes,
        'coupling_dB': coup,
        'node_absorption_dB': nodes,
        'propagation_dB': prop,
        'bend_dB': bends,
        'total_dB': total,
        'computational_scattering_dB': f'N/A — directed scattering IS the computation',
        'snr_dB': LASER_POWER_DBM - total - NOISE_FLOOR_DBM
    }

def max_depth(node_loss, coupling_loss, wg_loss=WG_PROPAGATION_LOSS):
    """Max nodes before SNR drops below threshold."""
    numerator = LASER_POWER_DBM - NOISE_FLOOR_DBM - REQUIRED_SNR_DB - coupling_loss
    denominator = node_loss + wg_loss * PATH_PER_NODE_CM + BENDS_PER_NODE * BEND_LOSS_PER_TURN
    return numerator / denominator

def run_node_centric_loss():
    results = {}

    results['paradigm_shift'] = {
        'old_model': 'Node insertion loss = 0.08 dB/node (treats computation as waste)',
        'new_model': 'Node absorption = 0.09 dB/node (only absorbed light is lost)',
        'directed_scattering': 'IS the computation — path integral summation of scattered fields',
        'note': (
            "The 0.08 dB/node 'insertion loss' from the spec was treating the computational "
            "element as a passive loss element. In VOPU, the node scatters light in a directed "
            "pattern that implements the weight. The scattered fields sum via path integral. "
            "Only absorbed or truly mode-mismatched light is lost."
        )
    }

    # Scenarios
    scenarios = {
        'baseline': {
            'node_loss': NODE_TRUE_LOSS,  # 0.09 dB absorption
            'coupling_loss': COUPLING_LOSS,
            'label': 'Node absorption only (directed scattering = computation)',
        },
        'optimized': {
            'node_loss': 0.03,  # lower absorption with better materials
            'coupling_loss': COUPLING_OPTIMIZED,
            'label': 'Optimized materials + mode-matched coupling',
        },
        'with_rsa': {
            'node_loss': NODE_TRUE_LOSS + RSA_TRANSPARENT_LOSS_DB,  # RSA zones below threshold
            'coupling_loss': COUPLING_LOSS,
            'label': 'With RSA zones (below threshold, transparent)',
        },
        'old_model_comparison': {
            'node_loss': 0.08,  # old "insertion loss" model
            'coupling_loss': COUPLING_LOSS,
            'label': 'Old model: 0.08 dB/node insertion loss (incorrect framing)',
        }
    }

    for name, sc in scenarios.items():
        max_d = max_depth(sc['node_loss'], sc['coupling_loss'])

        # Breakdown at key depths
        breakdown = {}
        for depth in [5, 10, 20, 50, 100, 500]:
            b = compute_budget(depth, sc['node_loss'], sc['coupling_loss'])
            breakdown[f'{depth}_nodes'] = b

        results[name] = {
            'label': sc['label'],
            'node_loss_model': f'{sc["node_loss"]:.4f} dB/node (absorption only)',
            'max_cascade_depth': float(max_d),
            'breakdown': breakdown
        }

    # Key comparison
    baseline = results['baseline']
    old = results['old_model_comparison']

    results['findings'] = {
        'node_loss_correction': {
            'old_insertion_loss_dB': 0.08,
            'corrected_absorption_dB': NODE_TRUE_LOSS,
            'note': 'Directed scattering is computation, not loss. Only absorption counts.'
        },
        'max_depth_baseline': baseline['max_cascade_depth'],
        'max_depth_optimized': results['optimized']['max_cascade_depth'],
        'max_depth_old_model': old['max_cascade_depth'],
        'loss_at_10_nodes': {
            'node_absorption': f"{baseline['breakdown']['10_nodes']['node_absorption_dB']:.3f} dB",
            'propagation': f"{baseline['breakdown']['10_nodes']['propagation_dB']:.4f} dB",
            'bends': f"{baseline['breakdown']['10_nodes']['bend_dB']:.4f} dB",
            'coupling': f"{baseline['breakdown']['10_nodes']['coupling_dB']:.1f} dB",
            'total': f"{baseline['breakdown']['10_nodes']['total_dB']:.3f} dB",
            'snr': f"{baseline['breakdown']['10_nodes']['snr_dB']:.1f} dB"
        },
        'implication': (
            f"When nodes are correctly modeled as computing elements (not loss elements), "
            f"the loss budget is dominated by coupling efficiency ({COUPLING_LOSS} dB) "
            f"and material absorption (~{NODE_TRUE_LOSS:.2f} dB/node). "
            f"Max cascade depth: ~{baseline['max_cascade_depth']:.0f} nodes (baseline), "
            f"~{results['optimized']['max_cascade_depth']:.0f} nodes (optimized). "
            f"The path integral summation of directed scattered fields IS the computation — "
            f"it's not loss, it's the answer."
        ),
        'evidence': 'E - reframed model; node absorption estimated from material properties'
    }

    return results

if __name__ == '__main__':
    results = run_node_centric_loss()
    print(json.dumps(results, indent=2, default=str))
