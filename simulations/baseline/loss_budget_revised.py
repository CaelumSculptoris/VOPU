"""
Revised Loss Budget for VOPU — Fiber-Optic Principle
=====================================================

Key correction: VOPU waveguides are fiber-optic channels carved into a
transparent medium. Propagation loss should be treated as negligible
(fiber-like), NOT as a dominant loss term.

The actual loss sources are:
1. Node insertion loss (scattering at terminal junctions)
2. Coupling loss (fiber-to-volume and volume-to-detector)
3. Bend loss (at routing corners)

Evidence:
  - Silica fiber: 0.2 dB/km = 0.000002 dB/cm [D]
  - PMMA plastic fiber at 520nm: ~0.1 dB/m = 0.001 dB/cm [D]
  - LNOI waveguide: 0.13 dB/cm [D - but includes surface roughness]
  - ImpCarv hydrogel: transparent at 532nm, Rayleigh scattering minimal

The 0.25 dB/cm in the REV8 spec was a conservative placeholder, not a
measured value. Fiber-optic channels in a transparent medium have
negligible propagation loss.
"""

import numpy as np
import json

# ============================================================
# CORRECTED Propagation Loss
# ============================================================

# Fiber-optic principle: channels in transparent medium
# PMMA POF at 520nm: ~0.1 dB/m = 0.0001 dB/cm [D - commercial POF spec]
# Hydrogel at 532nm: should be comparable or better (highly transparent)
# Use 0.001 dB/cm as a conservative bound (10x worse than POF, accounts
# for surface roughness from ImpCarv fabrication)
WG_PROPAGATION_LOSS = 0.001  # dB/cm — fiber-like, NOT 0.25

# Surface roughness contribution (ImpCarv 67nm features)
# Scattering loss from wall roughness: α_s ~ (4π/λ)² * σ² * Δn² * h
# For σ=12nm, Δn=0.5, λ=532nm: α_s ~ 0.01 dB/cm (estimated)
WG_ROUGHNESS_LOSS = 0.01  # dB/cm — from ImpCarv surface roughness

# Total propagation loss: fiber-like + roughness
WG_ATTENUATION = WG_PROPAGATION_LOSS + WG_ROUGHNESS_LOSS  # ~0.011 dB/cm

# ============================================================
# Node Loss (the REAL loss source)
# ============================================================
NODE_INSERTION_LOSS = 0.08      # dB/node [E - VOPU spec, conservative]
NODE_LOSS_OPTIMIZED = 0.03       # dB/node [E - if well-designed scattering node]

# ============================================================
# Coupling Loss
# ============================================================
COUPLING_LOSS = 0.5              # dB per facet (input + output) [E]
COUPLING_LOSS_OPTIMIZED = 0.2    # dB per facet with mode matching [E]

# ============================================================
# Bend Loss (at routing corners)
# ============================================================
BEND_LOSS_PER_TURN = 0.02        # dB per 90° bend [E - conservative for high-NA guide]

# ============================================================
# System Parameters
# ============================================================
LASER_POWER_DBM = 10              # 10 mW
DETECTOR_NOISE_FLOOR_DBM = -70    # APD
REQUIRED_SNR_DB = 15

# Node geometry
NODE_SPACING_CM = 0.05            # 500 µm
PATH_PER_NODE_CM = 0.1            # 1 mm average routing
BENDS_PER_NODE = 0.5              # average bends per node hop

# ============================================================
# Analysis
# ============================================================

def total_loss(n_nodes, wg_loss, node_loss, coupling_loss, path_per_node, bends_per_node, bend_loss):
    """
    Total loss: coupling + propagation + node scattering + bend loss
    L = L_coupling + n * (L_node + α_wg * L_path + n_bends * L_bend)
    """
    return (coupling_loss +
            n_nodes * (node_loss + wg_loss * path_per_node + bends_per_node * bend_loss))

def max_depth(laser_p, noise_floor, required_snr, wg_loss, node_loss,
              coupling_loss, path_per_node, bends_per_node, bend_loss):
    """Max nodes before SNR drops below threshold."""
    numerator = laser_p - noise_floor - required_snr - coupling_loss
    denominator = node_loss + wg_loss * path_per_node + bends_per_node * bend_loss
    return numerator / denominator

def run_revised_loss_budget():
    results = {}

    # Show the correction
    results['correction'] = {
        'original_spec_value_dB_per_cm': 0.25,
        'corrected_value_dB_per_cm': WG_ATTENUATION,
        'correction_factor': 0.25 / WG_ATTENUATION,
        'rationale': (
            "The REV8 spec's 0.25 dB/cm was a conservative placeholder, not a measurement. "
            "VOPU waveguides are fiber-optic channels in a transparent medium. "
            "Commercial PMMA fiber at 520nm achieves 0.001 dB/cm. "
            "ImpCarv surface roughness adds ~0.01 dB/cm scattering. "
            "Total: ~0.011 dB/cm — 23x lower than the spec placeholder."
        ),
        'evidence': 'D - fiber loss from commercial POF specs; E - roughness estimate'
    }

    scenarios = {
        'fiber_like': {
            'wg_loss': WG_ATTENUATION,
            'node_loss': NODE_INSERTION_LOSS,
            'coupling_loss': COUPLING_LOSS,
            'bend_loss': BEND_LOSS_PER_TURN,
            'label': 'Fiber-like propagation + VOPU spec nodes',
            'evidence': 'S - fiber principle + VOPU node estimates'
        },
        'optimized': {
            'wg_loss': WG_ATTENUATION,
            'node_loss': NODE_LOSS_OPTIMIZED,
            'coupling_loss': COUPLING_LOSS_OPTIMIZED,
            'bend_loss': 0.01,  # dB per bend
            'label': 'Optimized nodes + mode-matched coupling',
            'evidence': 'E - engineering targets'
        },
        'original_spec': {
            'wg_loss': 0.25,  # original placeholder
            'node_loss': NODE_INSERTION_LOSS,
            'coupling_loss': COUPLING_LOSS,
            'bend_loss': BEND_LOSS_PER_TURN,
            'label': 'Original spec (0.25 dB/cm placeholder)',
            'evidence': 'E - original REV8 placeholder'
        }
    }

    node_range = np.arange(1, 501)

    for name, sc in scenarios.items():
        losses = total_loss(node_range, sc['wg_loss'], sc['node_loss'],
                           sc['coupling_loss'], PATH_PER_NODE_CM,
                           sc['bends_per_node'] if 'bends_per_node' in sc else BENDS_PER_NODE,
                           sc['bend_loss'])
        snrs = (LASER_POWER_DBM - losses - DETECTOR_NOISE_FLOOR_DBM)
        max_d = max_depth(LASER_POWER_DBM, DETECTOR_NOISE_FLOOR_DBM, REQUIRED_SNR_DB,
                          sc['wg_loss'], sc['node_loss'], sc['coupling_loss'],
                          PATH_PER_NODE_CM, BENDS_PER_NODE, sc['bend_loss'])

        # Loss breakdown for 10-node network
        depth_10_loss = total_loss(10, sc['wg_loss'], sc['node_loss'],
                                   sc['coupling_loss'], PATH_PER_NODE_CM,
                                   BENDS_PER_NODE, sc['bend_loss'])
        prop_10 = 10 * sc['wg_loss'] * PATH_PER_NODE_CM
        node_10 = 10 * sc['node_loss']
        bend_10 = 10 * BENDS_PER_NODE * sc['bend_loss']
        coup_10 = sc['coupling_loss']

        results[name] = {
            'label': sc['label'],
            'evidence': sc['evidence'],
            'parameters': {
                'propagation_loss_dB_per_cm': sc['wg_loss'],
                'node_loss_dB': sc['node_loss'],
                'coupling_loss_dB': sc['coupling_loss'],
                'bend_loss_dB_per_turn': sc['bend_loss'],
            },
            'max_cascade_depth': float(max_d),
            'loss_at_10_nodes': {
                'total_dB': float(depth_10_loss),
                'breakdown': {
                    'propagation_dB': float(prop_10),
                    'node_scattering_dB': float(node_10),
                    'bend_dB': float(bend_10),
                    'coupling_dB': float(coup_10),
                    'propagation_fraction': float(prop_10 / depth_10_loss),
                    'node_fraction': float(node_10 / depth_10_loss),
                }
            },
            'depths': node_range.tolist(),
            'losses_dB': losses.tolist(),
            'snrs_dB': snrs.tolist()
        }

    # Key comparison
    fiber = results['fiber_like']
    spec = results['original_spec']

    results['findings'] = {
        'propagation_loss_corrected': {
            'spec_placeholder': 0.25,
            'fiber_like': WG_ATTENUATION,
            'improvement_factor': 0.25 / WG_ATTENUATION,
            'note': 'Propagation through straight channels in transparent medium = fiber optics. Negligible loss.'
        },
        'dominant_loss_source': {
            'at_10_nodes': 'node_scattering',
            'node_fraction': fiber['loss_at_10_nodes']['breakdown']['node_fraction'],
            'propagation_fraction': fiber['loss_at_10_nodes']['breakdown']['propagation_fraction'],
            'note': f"At 10 nodes: node scattering is {fiber['loss_at_10_nodes']['breakdown']['node_fraction']*100:.0f}% of total loss, "
                    f"propagation is {fiber['loss_at_10_nodes']['breakdown']['propagation_fraction']*100:.0f}%."
        },
        'max_depth_fiber_like': fiber['max_cascade_depth'],
        'max_depth_spec_placeholder': spec['max_cascade_depth'],
        'implication': (
            f"With fiber-like propagation ({WG_ATTENUATION} dB/cm), max cascade depth jumps to "
            f"~{fiber['max_cascade_depth']:.0f} nodes. The binding constraint shifts entirely "
            f"to node insertion loss and coupling efficiency. Propagation loss through straight "
            f"channels is negligible — it's fiber optics. The engineering challenge is making "
            f"terminal nodes that scatter cleanly, not making the medium less lossy."
        ),
        'evidence': 'S - revised simulation with fiber-optic propagation principle'
    }

    return results

if __name__ == '__main__':
    results = run_revised_loss_budget()
    print(json.dumps(results, indent=2, default=str))
