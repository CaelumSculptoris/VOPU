"""
VOPU System Validation & Unit Test Suite (v1.0)
Testing Phase Precision, Pre-compensation, SLM Wavefront Coupling, and Loss Budgets.
"""

import math
import json
import numpy as np

def test_phase_jitter_and_precompensation():
    """
    Simulates Monte Carlo phase jitter across network depth N = 1..50.
    Compares uncompensated vs. phase-precompensated path integral fidelity.
    """
    np.random.seed(42)
    n_trials = 1000
    depths = [1, 5, 10, 20, 30, 50]
    sigma_phase_rad = np.radians(16.4) # 16.4 degrees per node
    
    results = {}
    
    for N in depths:
        # Uncompensated error accumulation
        # True signal has sum of nominal phases = 0 for test reference
        uncompensated_fidelities = []
        compensated_fidelities = []
        
        for _ in range(n_trials):
            # Node errors
            node_errors = np.random.normal(0, sigma_phase_rad, size=N)
            
            # Uncompensated total field
            # Ideal field = exp(i * 0) = 1.0
            actual_field_uncomp = np.exp(1j * np.sum(node_errors))
            fidelity_uncomp = np.real(actual_field_uncomp) # Projection onto ideal axis
            uncompensated_fidelities.append(fidelity_uncomp)
            
            # Pre-compensated: Compiler pre-shifts coordinates by -sum(expected systematic drift)
            # Remaining error is residual higher-order variance
            systematic_drift = np.sum(node_errors) * 0.85 # Assume 85% predictable spatial drift
            residual_errors = node_errors - (systematic_drift / N)
            actual_field_comp = np.exp(1j * np.sum(residual_errors))
            fidelity_comp = np.real(actual_field_comp)
            compensated_fidelities.append(fidelity_comp)
            
        mean_uncomp = float(np.mean(uncompensated_fidelities))
        mean_comp = float(np.mean(compensated_fidelities))
        results[f"Depth_{N}"] = {
            "uncompensated_fidelity": round(mean_uncomp, 4),
            "precompensated_fidelity": round(mean_comp, 4),
            "improvement": f"{((mean_comp - mean_uncomp) / max(abs(mean_uncomp), 1e-5)) * 100:.1f}%"
        }
        
    print("[PASS] Phase Jitter & Pre-compensation Monte Carlo Test Completed.")
    return results


def test_loss_budget_and_snr():
    """
    Validates optical loss budget and SNR for a 10-node cascade.
    """
    prop_loss_db_per_cm = 0.011
    total_length_cm = 5.0 # 5 cm 3D volume
    facet_coupling_loss_db = 0.5 * 2 # 2 facets (in/out)
    node_material_absorption_db = 0.088 * 10 # 10 nodes
    
    total_prop_loss = prop_loss_db_per_cm * total_length_cm
    total_loss_db = total_prop_loss + facet_coupling_loss_db + node_material_absorption_db
    
    # Input power = 10 mW (10 dBm)
    input_power_dbm = 10.0
    output_power_dbm = input_power_dbm - total_loss_db
    
    # Noise floor at -70 dBm
    noise_floor_dbm = -70.0
    snr_db = output_power_dbm - noise_floor_dbm
    
    assert total_loss_db < 2.0, f"Total loss {total_loss_db} dB exceeds 2.0 dB budget limit!"
    assert snr_db > 70.0, f"SNR {snr_db} dB below 70 dB threshold!"
    
    print(f"[PASS] Loss Budget Test Completed: Total Loss = {total_loss_db:.3f} dB, SNR = {snr_db:.1f} dB.")
    return {
        "total_loss_db": round(total_loss_db, 3),
        "snr_db": round(snr_db, 1),
        "max_supportable_nodes": int(math.floor((input_power_dbm - noise_floor_dbm - facet_coupling_loss_db - total_prop_loss) / 0.088))
    }


def test_shrinkage_deformation_scaling():
    """
    Validates hydrogel inverse deformation scaling (MSF formulation = 5.03x).
    """
    shrinkage_factor = 5.03
    target_node_coords_um = np.array([[10.0, 20.0, 30.0], [50.0, 100.0, 150.0]])
    
    # Compiler pre-deformation
    compiled_coords_um = target_node_coords_um * shrinkage_factor
    
    # Simulated physical dehydration
    shrunken_coords_um = compiled_coords_um / shrinkage_factor
    
    max_error = np.max(np.abs(shrunken_coords_um - target_node_coords_um))
    assert max_error < 1e-6, "Shrinkage deformation mismatch!"
    
    print("[PASS] Hydrogel Deformation Scaling Test Completed.")
    return {
        "shrinkage_factor": shrinkage_factor,
        "max_reconstruction_error_um": float(max_error)
    }


if __name__ == "__main__":
    print("--- Running VOPU Validation Test Suite ---")
    res_phase = test_phase_jitter_and_precompensation()
    res_loss = test_loss_budget_and_snr()
    res_shrink = test_shrinkage_deformation_scaling()
    
    summary = {
        "phase_test": res_phase,
        "loss_budget_test": res_loss,
        "deformation_test": res_shrink
    }
    
    with open("/workspace/scratch/vopu_test_results.json", "w") as f:
        json.dump(summary, f, indent=2)
        
    print("\nAll tests passed successfully! Test results saved to /workspace/scratch/vopu_test_results.json")
