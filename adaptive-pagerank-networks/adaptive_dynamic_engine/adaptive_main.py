import json
import sys
import os

# =========================================================================
# SYSTEM DIR PATH MATRIX OVERRIDE
# =========================================================================
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)  # Steps out into v1-experimental-framework

sys.path.append(parent_dir)

# Import shared dependencies from your structured directories
from output.simple_graphs import spider_trap, star_graph
from adaptive_dynamic_engine.adaptive_pagerank import run_adaptive_power_iteration

def execute_experiments():
    """
    Runs sandbox simulations for the Adaptive Core across scaling profiles
    from N=11 to N=5000, mimicking baseline experimental structure.
    """
    network_sizes = [11, 50, 100, 500, 1000, 5000]
    
    # Formulate pure metric logging output tree
    adaptive_output = {
        "adaptive_core": {
            "spider_trap": {},
            "star_graph": {}
        }
    }
    
    print("--- INITIALIZING ADAPTIVE ENGINE SANDBOX BENCHMARKS ---")
    
    for size in network_sizes:
        print(f"\n[Evaluating Scaling Interface: {size} Nodes]")
        
        # Load standard synthetic test network graphs
        graphs_map = {
            "spider_trap": spider_trap(size),
            "star_graph": star_graph(size)
        }
        
        for topology_name, active_matrix in graphs_map.items():
            print(f"Running System Verification: {topology_name.upper()}")
            
            # Execute power iteration against raw mathematical signatures
            _, loops, density, final_alpha = run_adaptive_power_iteration(
                nodes_count=size,
                connection_graph=active_matrix
            )
            
            # Record results data matrix payload arrays
            adaptive_output["adaptive_core"][topology_name][str(size)] = {
                "graph_density_rho": round(density, 6),
                "calculated_damping_factor": round(final_alpha, 4),
                "convergence_loops": loops
            }
            print(f" -> Result: Loops={loops} | Density={density:.6f} | Alpha={final_alpha:.4f}")
            
    # Build structural JSON output path inside data directory folder
    export_path = os.path.join(parent_dir, 'output', 'adaptive_experiment_results.json')
    os.makedirs(os.path.dirname(export_path), exist_ok=True)
    
    with open(export_path, 'w', encoding='utf-8') as json_file:
        json.dump(adaptive_output, json_file, indent=4)
        
    print(f"\n[SUCCESS] Verification metrics fully logged to: {export_path}\n")

if __name__ == "__main__":
    execute_experiments()
