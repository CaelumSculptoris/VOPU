"""
Mode Analysis for Post-Shrinkage VOPU Waveguides
=================================================

Computes V-number, single-mode condition, mode field diameter, and
numerical aperture for waveguides fabricated by Implosion Carving.

Reference parameters from VOPU Architecture (REV8):
  - Wavelength: 532 nm
  - Substrate index: ~1.48
  - Peak index contrast: ~0.40

ImpCarv demonstrated parameters (Yang et al., Nature Photonics 2026):
  - Post-dehydration gel index: ~1.5
  - Air-filled vacancy contrast: ~Δn = 0.5
  - Lateral vacancy width: 67 ± 12 nm FWHM
  - Axial step: 22 ± 2 nm

Evidence labels noted inline.
"""

import numpy as np
import json
from pathlib import Path

# ============================================================
# Physical Constants
# ============================================================
C = 2.99792458e8          # speed of light, m/s
PI = np.pi

# ============================================================
# Reference Parameters
# ============================================================

# VOPU REV8 reference parameters [E - estimated from architecture spec]
WAVELENGTH = 532e-9        # 532 nm [D - from ImpCarv paper]
N_SUBSTRATE = 1.48         # substrate refractive index [E - VOPU spec]
DELTA_N_VOPU = 0.40        # peak index contrast [E - VOPU spec]

# ImpCarv demonstrated parameters [D - from Yang et al. 2026]
N_GEL_IMPCARV = 1.5        # post-dehydration gel index [D]
N_AIR = 1.0                # air-filled vacancy [D]
DELTA_N_IMPCARV = N_GEL_IMPCARV - N_AIR  # ≈ 0.5 [D]

# Waveguide geometry range (post-shrinkage)
# ImpCarv demonstrated 67 nm lateral features; VOPU waveguides will be wider
WG_WIDTH_MIN = 200e-9       # 200 nm (aggressive)
WG_WIDTH_MAX = 2000e-9      # 2 µm (conservative)
WG_WIDTHS = np.linspace(WG_WIDTH_MIN, WG_WIDTH_MAX, 500)

# ============================================================
# Mode Analysis Functions
# ============================================================

def v_number(wavelength, radius, n_core, n_clad):
    """
    Compute the V-number (normalized frequency) for a step-index waveguide.
    
    V = (2π/λ) * a * NA
    where NA = sqrt(n_core² - n_clad²)
    
    Single-mode condition: V < 2.405 (for step-index fiber/circular guide)
    For rectangular/slab: V < π/2 for single TE mode
    
    Returns V-number and NA.
    """
    NA = np.sqrt(n_core**2 - n_clad**2)
    V = (2 * PI / wavelength) * radius * NA
    return V, NA

def single_mode_radius_max(wavelength, n_core, n_clad, V_cutoff=2.405):
    """
    Maximum radius for single-mode operation.
    a_max = V_cutoff * λ / (2π * NA)
    """
    NA = np.sqrt(n_core**2 - n_clad**2)
    return V_cutoff * wavelength / (2 * PI * NA)

def mode_field_diameter(wavelength, a, n_core, n_clad):
    """
    Approximate mode field diameter (MFD) using Marcuse formula:
    w/a = 0.65 + 1.619/V^(3/2) + 2.879/V^6
    
    Valid for step-index fiber near cutoff.
    """
    V, _ = v_number(wavelength, a, n_core, n_clad)
    if V < 0.1:
        return 2 * a  # fallback
    ratio = 0.65 + 1.619 / V**1.5 + 2.879 / V**6
    return 2 * a * ratio

def confining_factor(wavelength, a, n_core, n_clad):
    """
    Approximate power confinement factor for step-index waveguide.
    Γ ≈ 1 - exp(-2 * V²) for rough estimate.
    """
    V, _ = v_number(wavelength, a, n_core, n_clad)
    return 1 - np.exp(-2 * V**2)

# ============================================================
# Run Analysis
# ============================================================

def run_mode_analysis():
    """Run complete mode analysis and return results dict."""
    results = {}
    
    # --- V-number vs waveguide width ---
    # Using VOPU parameters (n_core = n_substrate + Δn, n_clad = n_substrate)
    n_core_vopu = N_SUBSTRATE + DELTA_N_VOPU  # 1.88
    n_clad_vopu = N_SUBSTRATE                  # 1.48
    
    # Using ImpCarv demonstrated parameters (gel/air)
    n_core_imp = N_GEL_IMPCARV                 # 1.5
    n_clad_imp = N_AIR                         # 1.0
    
    V_vopu, NA_vopu = v_number(WAVELENGTH, WG_WIDTHS / 2, n_core_vopu, n_clad_vopu)
    V_imp, NA_imp = v_number(WAVELENGTH, WG_WIDTHS / 2, n_core_imp, n_clad_imp)
    
    results['v_number'] = {
        'wavelength_nm': WAVELENGTH * 1e9,
        'widths_nm': (WG_WIDTHS * 1e9).tolist(),
        'V_vopu': V_vopu.tolist(),
        'NA_vopu': float(NA_vopu),
        'V_impcarv': V_imp.tolist(),
        'NA_impcarv': float(NA_imp),
        'cutoff_V': 2.405,
        'note': 'Single-mode condition: V < 2.405 (circular) or V < π/2 (slab)'
    }
    
    # --- Single-mode maximum radius ---
    a_max_vopu = single_mode_radius_max(WAVELENGTH, n_core_vopu, n_clad_vopu)
    a_max_imp = single_mode_radius_max(WAVELENGTH, n_core_imp, n_clad_imp)
    
    results['single_mode_max'] = {
        'vopu': {
            'n_core': n_core_vopu,
            'n_clad': n_clad_vopu,
            'NA': float(NA_vopu),
            'max_radius_nm': a_max_vopu * 1e9,
            'max_diameter_nm': 2 * a_max_vopu * 1e9,
            'evidence': 'E - first-order calculation from VOPU spec parameters'
        },
        'impcarv': {
            'n_core': n_core_imp,
            'n_clad': n_clad_imp,
            'NA': float(NA_imp),
            'max_radius_nm': a_max_imp * 1e9,
            'max_diameter_nm': 2 * a_max_imp * 1e9,
            'evidence': 'D - calculation from ImpCarv demonstrated parameters'
        }
    }
    
    # --- Mode field diameter for key widths ---
    key_widths = [300e-9, 500e-9, 800e-9, 1000e-9]  # 300, 500, 800, 1000 nm
    mfd_results = []
    for w in key_widths:
        V_v, _ = v_number(WAVELENGTH, w/2, n_core_vopu, n_clad_vopu)
        V_i, _ = v_number(WAVELENGTH, w/2, n_core_imp, n_clad_imp)
        mfd_v = mode_field_diameter(WAVELENGTH, w/2, n_core_vopu, n_clad_vopu)
        mfd_i = mode_field_diameter(WAVELENGTH, w/2, n_core_imp, n_clad_imp)
        cf_v = confining_factor(WAVELENGTH, w/2, n_core_vopu, n_clad_vopu)
        cf_i = confining_factor(WAVELENGTH, w/2, n_core_imp, n_clad_imp)
        mfd_results.append({
            'width_nm': w * 1e9,
            'V_vopu': float(V_v),
            'V_impcarv': float(V_i),
            'single_mode_vopu': bool(V_v < 2.405),
            'single_mode_impcarv': bool(V_i < 2.405),
            'MFD_vopu_nm': float(mfd_v * 1e9),
            'MFD_impcarv_nm': float(mfd_i * 1e9),
            'confinement_vopu': float(cf_v),
            'confinement_impcarv': float(cf_i)
        })
    results['mode_field_diameters'] = mfd_results
    
    # --- Key findings ---
    results['findings'] = {
        'vopu_single_mode_max_diameter_nm': 2 * a_max_vopu * 1e9,
        'impcarv_single_mode_max_diameter_nm': 2 * a_max_imp * 1e9,
        'vopu_NA': float(NA_vopu),
        'impcarv_NA': float(NA_imp),
        'implication': (
            f"With VOPU's high index contrast (Δn={DELTA_N_VOPU}, NA={NA_vopu:.3f}), "
            f"single-mode waveguides must be < {2*a_max_vopu*1e9:.0f} nm diameter. "
            f"ImpCarv has demonstrated {67}nm features, making this achievable. "
            f"However, mode field diameter will be larger than the physical guide, "
            f"requiring careful coupling design."
        ),
        'evidence': 'S - simulated from first-order waveguide theory'
    }
    
    return results

if __name__ == '__main__':
    results = run_mode_analysis()
    print(json.dumps(results, indent=2))
