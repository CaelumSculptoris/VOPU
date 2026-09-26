"""
VOPU Baseline Simulation Runner
================================

Runs all baseline simulations, generates plots, and produces a summary report.
"""

import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

from .mode_analysis import run_mode_analysis
from .loss_budget import run_loss_budget
from .phase_budget import run_phase_budget
from .nonlinear_estimates import run_nonlinear_analysis
from .cascability import run_cascability

PLOT_DIR = Path(__file__).parent / 'plots'
PLOT_DIR.mkdir(exist_ok=True)

def plot_v_number(results):
    """Plot V-number vs waveguide width."""
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    widths = np.array(results['v_number']['widths_nm'])
    V_vopu = np.array(results['v_number']['V_vopu'])
    V_imp = np.array(results['v_number']['V_impcarv'])
    
    ax.plot(widths, V_vopu, 'b-', linewidth=2, label=f"VOPU params (NA={results['v_number']['NA_vopu']:.3f})")
    ax.plot(widths, V_imp, 'r--', linewidth=2, label=f"ImpCarv params (NA={results['v_number']['NA_impcarv']:.3f})")
    ax.axhline(y=2.405, color='k', linestyle=':', linewidth=1, label='Single-mode cutoff (V=2.405)')
    
    ax.set_xlabel('Waveguide Diameter (nm)', fontsize=12)
    ax.set_ylabel('V-number', fontsize=12)
    ax.set_title('VOPU Mode Analysis: Single-Mode Condition', fontsize=14)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(200, 2000)
    ax.set_ylim(0, 15)
    
    fig.tight_layout()
    fig.savefig(PLOT_DIR / 'v_number.png', dpi=150)
    plt.close(fig)

def plot_loss_budget(results):
    """Plot loss budget and SNR vs depth."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    colors = {
        'vopu_optimistic': ('b', '-'),
        'vopu_conservative': ('g', '--'),
        'vopu_pessimistic': ('r', ':'),
        'vopu_best_case': ('purple', '-.')
    }
    
    for name, (color, style) in colors.items():
        sc = results[name]
        depths = np.array(sc['depths'])
        losses = np.array(sc['losses_dB'])
        snrs = np.array(sc['snrs_dB'])
        
        ax1.plot(depths, losses, color=color, linestyle=style, linewidth=2,
                label=f"{sc['label']} (max depth: {sc['max_cascade_depth']:.0f})")
        ax2.plot(depths, snrs, color=color, linestyle=style, linewidth=2,
                label=sc['label'])
    
    ax2.axhline(y=15, color='k', linestyle=':', linewidth=1, label='Required SNR (15 dB)')
    
    ax1.set_xlabel('Network Depth (nodes)', fontsize=12)
    ax1.set_ylabel('Total Insertion Loss (dB)', fontsize=12)
    ax1.set_title('VOPU Loss Budget: Cascaded Network', fontsize=14)
    ax1.legend(fontsize=8)
    ax1.grid(True, alpha=0.3)
    
    ax2.set_xlabel('Network Depth (nodes)', fontsize=12)
    ax2.set_ylabel('SNR (dB)', fontsize=12)
    ax2.set_title('VOPU SNR vs Network Depth', fontsize=14)
    ax2.legend(fontsize=8)
    ax2.grid(True, alpha=0.3)
    
    fig.tight_layout()
    fig.savefig(PLOT_DIR / 'loss_budget.png', dpi=150)
    plt.close(fig)

def plot_phase_budget(results):
    """Plot phase error accumulation vs depth."""
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    
    depths = np.array(results['cascaded']['depths'])
    sigma_deg = np.array(results['cascaded']['sigma_total_degrees'])
    
    ax.plot(depths, sigma_deg, 'b-', linewidth=2, label='Cumulative phase error (1σ)')
    ax.axhline(y=45, color='r', linestyle='--', linewidth=1.5, label='Tolerance (45°)')
    ax.axhline(y=22.5, color='orange', linestyle='--', linewidth=1.5, label='Strict tolerance (22.5°)')
    
    # Mark max depths
    ax.axvline(x=results['cascaded']['max_depth_45deg'], color='r', linestyle=':', alpha=0.5)
    ax.axvline(x=results['cascaded']['max_depth_22.5deg'], color='orange', linestyle=':', alpha=0.5)
    
    ax.set_xlabel('Network Depth (nodes)', fontsize=12)
    ax.set_ylabel('Phase Error (degrees, 1σ)', fontsize=12)
    ax.set_title('VOPU Phase Error Accumulation', fontsize=14)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 200)
    ax.set_ylim(0, max(sigma_deg)*1.1)
    
    fig.tight_layout()
    fig.savefig(PLOT_DIR / 'phase_budget.png', dpi=150)
    plt.close(fig)

def plot_nonlinear(results):
    """Plot XPM phase shift vs power for different materials."""
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    
    xpm = results['xpm_phase_shift']['materials']
    colors = {
        'silicon_n2': ('b', '-'),
        'pmma_n2': ('g', '--'),
        'doped_polymer_n2': ('r', '-'),
        'hydrogel_thermal_n2': ('purple', ':'),
    }
    
    for mat_name, (color, style) in colors.items():
        mat = xpm[mat_name]
        powers = np.array(mat['powers_mW'])
        phases = np.array(mat['phase_shifts_deg'])
        ax.plot(powers, phases, color=color, linestyle=style, linewidth=2,
                label=f"{mat_name} (n2={mat['n2_m2_per_W']:.0e})")
    
    ax.axhline(y=45, color='k', linestyle='--', linewidth=1, label='Useful threshold (45°)')
    ax.axhline(y=0.57, color='gray', linestyle=':', linewidth=1, label='Detectable (0.01 rad)')
    
    ax.set_xlabel('Guided Power (mW)', fontsize=12)
    ax.set_ylabel('XPM Phase Shift (degrees)', fontsize=12)
    ax.set_title('VOPU XPM Phase Shift: Q/K Interaction Feasibility', fontsize=14)
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlim(1e-3, 100)
    ax.set_ylim(1e-4, 1e4)
    
    fig.tight_layout()
    fig.savefig(PLOT_DIR / 'xpm_phase_shift.png', dpi=150)
    plt.close(fig)

def plot_cascability(results):
    """Plot combined fidelity vs depth."""
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    
    depths = np.array(results['combined_fidelity']['depths'])
    fidelity = np.array(results['combined_fidelity']['fidelity'])
    snr_norm = np.array(results['combined_fidelity']['snr_normalized'])
    phase_norm = np.array(results['combined_fidelity']['phase_normalized'])
    
    ax.plot(depths, fidelity, 'k-', linewidth=2.5, label='Combined fidelity')
    ax.plot(depths, snr_norm, 'b--', linewidth=1.5, label='SNR-limited (normalized)')
    ax.plot(depths, phase_norm, 'r--', linewidth=1.5, label='Phase-limited (normalized)')
    ax.axhline(y=0.9, color='green', linestyle=':', linewidth=1, label='90% fidelity')
    ax.axhline(y=0.5, color='orange', linestyle=':', linewidth=1, label='50% fidelity')
    
    ax.axvline(x=results['combined_fidelity']['max_depth_90pct'], color='green', linestyle=':', alpha=0.5)
    ax.axvline(x=results['combined_fidelity']['max_depth_50pct'], color='orange', linestyle=':', alpha=0.5)
    
    ax.set_xlabel('Network Depth (nodes)', fontsize=12)
    ax.set_ylabel('Normalized Fidelity', fontsize=12)
    ax.set_title('VOPU Cascability: Combined Loss/Phase Budget', fontsize=14)
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 200)
    ax.set_ylim(0, 1.1)
    
    fig.tight_layout()
    fig.savefig(PLOT_DIR / 'cascability.png', dpi=150)
    plt.close(fig)

def run_all():
    """Run all simulations, generate plots, and produce summary report."""
    print("=" * 70)
    print("VOPU Baseline Physics Simulations")
    print("=" * 70)
    
    print("\n[1/5] Mode Analysis...")
    mode_results = run_mode_analysis()
    plot_v_number(mode_results)
    print(f"  VOPU single-mode max diameter: {mode_results['findings']['vopu_single_mode_max_diameter_nm']:.0f} nm")
    print(f"  ImpCarv single-mode max diameter: {mode_results['findings']['impcarv_single_mode_max_diameter_nm']:.0f} nm")
    print(f"  VOPU NA: {mode_results['findings']['vopu_NA']:.3f}")
    
    print("\n[2/5] Loss Budget...")
    loss_results = run_loss_budget()
    plot_loss_budget(loss_results)
    for name in ['vopu_optimistic', 'vopu_conservative', 'vopu_pessimistic', 'vopu_best_case']:
        print(f"  {name}: max depth = {loss_results[name]['max_cascade_depth']:.0f} nodes")
    
    print("\n[3/5] Phase Budget...")
    phase_results = run_phase_budget()
    plot_phase_budget(phase_results)
    print(f"  Dominant error source: {phase_results['findings']['dominant_error_source']}")
    print(f"  Max depth (45° tolerance): {phase_results['cascaded']['max_depth_45deg']:.0f} nodes")
    print(f"  Max depth (22.5° tolerance): {phase_results['cascaded']['max_depth_22.5deg']:.0f} nodes")
    
    print("\n[4/5] Nonlinear Estimates...")
    nonlinear_results = run_nonlinear_analysis()
    plot_nonlinear(nonlinear_results)
    print(f"  RSA threshold power: {nonlinear_results['rsa_thresholding']['threshold_power_nW']:.2f} nW")
    print(f"  XPM 45° power (doped polymer): {nonlinear_results['xpm_phase_shift']['findings']['doped_power_for_45deg']:.2f} mW")
    print(f"  XPM 45° power (PMMA): {nonlinear_results['xpm_phase_shift']['findings']['pmma_power_for_45deg']:.1f} mW")
    
    print("\n[5/5] Cascability Analysis...")
    cascability_results = run_cascability()
    plot_cascability(cascability_results)
    print(f"  Binding constraint: {cascability_results['findings']['binding_constraint']}")
    print(f"  Binding value: {cascability_results['findings']['binding_value']:.0f} nodes")
    print(f"  Max depth (90% fidelity): {cascability_results['findings']['max_depth_90pct_fidelity']} nodes")
    print(f"  Max depth (50% fidelity): {cascability_results['findings']['max_depth_50pct_fidelity']} nodes")
    print(f"  Go/No-Go: {cascability_results['findings']['go_no_go']['proceed_to_linear_demonstrator']}")
    
    # Compile full report
    full_report = {
        'mode_analysis': mode_results,
        'loss_budget': loss_results,
        'phase_budget': phase_results,
        'nonlinear_estimates': nonlinear_results,
        'cascability': cascability_results
    }
    
    # Save results JSON
    output_path = Path(__file__).parent / 'results.json'
    with open(output_path, 'w') as f:
        json.dump(full_report, f, indent=2, default=str)
    
    print(f"\nResults saved to {output_path}")
    print(f"Plots saved to {PLOT_DIR}")
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(cascability_results['findings']['implication'])
    
    return full_report

if __name__ == '__main__':
    run_all()
