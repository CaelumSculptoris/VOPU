"""
Loss Budget and Cascability Analysis for VOPU
==============================================

Computes the total optical loss budget for cascaded terminal nodes and
determines the maximum network depth before signal-to-noise ratio (SNR)
becomes unusable.

Reference parameters from VOPU Architecture (REV8):
  - Waveguide attenuation: 0.25 dB/cm [E]
  - Node insertion loss: 0.08 dB/node [E]
  - Wavelength: 532 nm

Literature-validated parameters:
  - LNOI waveguide loss: 0.13 dB/cm [D - arXiv:2006.11562]
  - Femtosecond-written BGO waveguide loss: 3-4 dB/cm [D]
  - Planar waveguide loss: <1 dB/cm [D - Agrawal lecture]

The 0.25 dB/cm target is aggressive but not impossible for high-quality
3D-written guides. We compute both optimistic and pessimistic scenarios.
"""

import numpy as np
import json

# ============================================================
# Reference Parameters
# ============================================================
WAVELENGTH_NM = 532

# VOPU REV8 reference [E - estimated]
WG_ATTENUATION_VOPU = 0.25       # dB/cm
NODE_INSERTION_LOSS = 0.08       # dB/node
COUPLING_LOSS = 0.5              # dB per facet (input + output)
DETECTOR_NOISE_FLOOR_DBM = -70   # dBm (typical APD)
LASER_POWER_DBM = 10             # dBm (10 mW, conservative)
REQUIRED_SNR_DB = 15             # dB (for reliable computation)

# Literature-validated bounds [D]
WG_ATTENUATION_LOW = 0.13        # dB/cm [D - LNOI, arXiv:2006.11562]
WG_ATTENUATION_HIGH = 3.0        # dB/cm [D - femtosecond-written BGO]
WG_ATTENUATION_PLANAR = 1.0      # dB/cm [D - Agrawal]

# Node spacing (assumed from architecture)
NODE_SPACING_CM = 0.05           # 500 µm between nodes (0.05 cm)
# Path length per node hop
PATH_PER_NODE_CM = 0.1           # 1 mm average routing path per node

# ============================================================
# Loss Budget Functions
# ============================================================

def total_loss(n_nodes, wg_attenuation, node_loss, coupling_loss, path_per_node):
    """
    Total insertion loss for a cascaded network of n_nodes.
    
    L_total = L_coupling + n * (L_node + α_wg * L_path_per_node)
    
    Returns loss in dB.
    """
    return coupling_loss + n_nodes * (node_loss + wg_attenuation * path_per_node)

def max_depth_snr(laser_power_dbm, noise_floor_dbm, required_snr,
                   wg_attenuation, node_loss, coupling_loss, path_per_node):
    """
    Maximum number of cascaded nodes before SNR drops below required threshold.
    
    SNR = P_laser - L_total - P_noise
    SNR >= required_snr
    
    Solving for n_nodes:
    n_max = (P_laser - P_noise - required_snr - L_coupling) / (L_node + α * L_path)
    """
    numerator = laser_power_dbm - noise_floor_dbm - required_snr - coupling_loss
    denominator = node_loss + wg_attenuation * path_per_node
    return numerator / denominator

def snr_vs_depth(n_nodes, laser_power_dbm, noise_floor_dbm,
                  wg_attenuation, node_loss, coupling_loss, path_per_node):
    """SNR as a function of network depth."""
    loss = total_loss(n_nodes, wg_attenuation, node_loss, coupling_loss, path_per_node)
    return laser_power_dbm - loss - noise_floor_dbm

def osnr_vs_depth(n_nodes, laser_power_dbm, noise_floor_dbm,
                   wg_attenuation, node_loss, coupling_loss, path_per_node):
    """Optical SNR (signal to shot noise) vs depth."""
    loss_db = total_loss(n_nodes, wg_attenuation, node_loss, coupling_loss, path_per_node)
    signal_dbm = laser_power_dbm - loss_db
    # Shot noise limited: SNR_shot = 10*log10(P_signal / (2*h*ν*B*P_signal))
    # Simplified: SNR ∝ P_signal (shot noise limited regime)
    return signal_dbm - noise_floor_dbm

# ============================================================
# Run Analysis
# ============================================================

def run_loss_budget():
    results = {}
    
    scenarios = {
        'vopu_optimistic': {
            'wg_attenuation': WG_ATTENUATION_VOPU,
            'node_loss': NODE_INSERTION_LOSS,
            'label': 'VOPU REV8 target parameters',
            'evidence': 'E - estimated from VOPU spec'
        },
        'vopu_conservative': {
            'wg_attenuation': WG_ATTENUATION_PLANAR,
            'node_loss': NODE_INSERTION_LOSS * 1.5,  # 0.12 dB/node
            'label': 'Conservative (planar-like loss, higher node loss)',
            'evidence': 'E - conservative estimate'
        },
        'vopu_pessimistic': {
            'wg_attenuation': WG_ATTENUATION_HIGH,
            'node_loss': 0.15,  # dB/node
            'label': 'Pessimistic (femtosecond-written loss)',
            'evidence': 'E - pessimistic bound from BGO waveguide data'
        },
        'vopu_best_case': {
            'wg_attenuation': WG_ATTENUATION_LOW,
            'node_loss': 0.05,  # dB/node (optimized)
            'label': 'Best case (LNOI-grade loss, optimized nodes)',
            'evidence': 'S - optimistic projection from demonstrated LNOI loss'
        }
    }
    
    node_range = np.arange(1, 201)
    
    for name, sc in scenarios.items():
        wg = sc['wg_attenuation']
        nl = sc['node_loss']
        
        losses = total_loss(node_range, wg, nl, COUPLING_LOSS, PATH_PER_NODE_CM)
        snrs = snr_vs_depth(node_range, LASER_POWER_DBM, DETECTOR_NOISE_FLOOR_DBM,
                           wg, nl, COUPLING_LOSS, PATH_PER_NODE_CM)
        max_depth = max_depth_snr(LASER_POWER_DBM, DETECTOR_NOISE_FLOOR_DBM,
                                   REQUIRED_SNR_DB, wg, nl, COUPLING_LOSS, PATH_PER_NODE_CM)
        
        # Loss budget breakdown for key depths
        depth_breakdown = []
        for depth in [1, 5, 10, 20, 50, 100]:
            if depth > max_depth:
                depth_breakdown.append({
                    'depth': depth,
                    'total_loss_dB': float(total_loss(depth, wg, nl, COUPLING_LOSS, PATH_PER_NODE_CM)),
                    'snr_dB': float(snr_vs_depth(depth, LASER_POWER_DBM, DETECTOR_NOISE_FLOOR_DBM,
                                                                wg, nl, COUPLING_LOSS, PATH_PER_NODE_CM)),
                    'status': 'below SNR threshold'
                })
            else:
                depth_breakdown.append({
                    'depth': depth,
                    'total_loss_dB': float(total_loss(depth, wg, nl, COUPLING_LOSS, PATH_PER_NODE_CM)),
                    'snr_dB': float(snr_vs_depth(depth, LASER_POWER_DBM, DETECTOR_NOISE_FLOOR_DBM,
                                                                wg, nl, COUPLING_LOSS, PATH_PER_NODE_CM)),
                    'status': 'usable'
                })
        
        results[name] = {
            'label': sc['label'],
            'evidence': sc['evidence'],
            'parameters': {
                'wg_attenuation_dB_per_cm': wg,
                'node_loss_dB': nl,
                'coupling_loss_dB': COUPLING_LOSS,
                'path_per_node_cm': PATH_PER_NODE_CM,
                'laser_power_dBm': LASER_POWER_DBM,
                'noise_floor_dBm': DETECTOR_NOISE_FLOOR_DBM,
                'required_snr_dB': REQUIRED_SNR_DB
            },
            'depths': node_range.tolist(),
            'losses_dB': losses.tolist(),
            'snrs_dB': snrs.tolist(),
            'max_cascade_depth': float(max_depth),
            'depth_breakdown': depth_breakdown
        }
    
    # --- Key findings ---
    opt = results['vopu_optimistic']
    cons = results['vopu_conservative']
    pess = results['vopu_pessimistic']
    best = results['vopu_best_case']
    
    results['findings'] = {
        'max_depth_optimistic': opt['max_cascade_depth'],
        'max_depth_conservative': cons['max_cascade_depth'],
        'max_depth_pessimistic': pess['max_cascade_depth'],
        'max_depth_best_case': best['max_cascade_depth'],
        'loss_per_node_optimistic_dB': NODE_INSERTION_LOSS + WG_ATTENUATION_VOPU * PATH_PER_NODE_CM,
        'loss_per_node_conservative_dB': cons['parameters']['node_loss_dB'] + WG_ATTENUATION_PLANAR * PATH_PER_NODE_CM,
        'loss_per_node_pessimistic_dB': 0.15 + WG_ATTENUATION_HIGH * PATH_PER_NODE_CM,
        'implication': (
            f"With VOPU target parameters, the maximum cascade depth is ~{opt['max_cascade_depth']:.0f} nodes "
            f"before SNR drops below {REQUIRED_SNR_DB} dB. "
            f"Conservative estimates give ~{cons['max_cascade_depth']:.0f} nodes. "
            f"The dominant loss mechanism is node insertion ({NODE_INSERTION_LOSS} dB/node), "
            f"contributing {NODE_INSERTION_LOSS/(NODE_INSERTION_LOSS+WG_ATTENUATION_VOPU*PATH_PER_NODE_CM)*100:.0f}% "
            f"of per-node loss. Reducing node insertion loss is the highest-impact optimization."
        ),
        'evidence': 'S - simulated from first-order loss budget'
    }
    
    return results

if __name__ == '__main__':
    results = run_loss_budget()
    print(json.dumps(results, indent=2))
