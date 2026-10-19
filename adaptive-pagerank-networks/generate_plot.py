"""
Adaptive PageRank Automated Plot Generation Engine
Submission Code Artifact for the Journal of High School Computer Science (JHCS)

This script reads from both experiment_results.json and adaptive_experiment_results.json
to reconstruct Figure 1 inside: output/scalability_convergence_curves.pdf
"""

import os
import json
import sys
import matplotlib.pyplot as plt

def main():
    # 1. Establish the directory path targeting your singular 'output' folder
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, "output")
    
    standard_json_path = os.path.join(output_dir, "experiment_results.json")
    adaptive_json_path = os.path.join(output_dir, "adaptive_experiment_results.json")
    
    # 2. Verify both files exist before attempting to read
    if not os.path.exists(standard_json_path):
        print(f"❌ ERROR: Missing standard file at: {standard_json_path}")
        sys.exit(1)
    if not os.path.exists(adaptive_json_path):
        print(f"❌ ERROR: Missing adaptive file at: {adaptive_json_path}")
        sys.exit(1)
        
    print("🔄 Dynamically reading tracking datasets from both files...")
    with open(standard_json_path, 'r') as f:
        std_data = json.load(f)
    with open(adaptive_json_path, 'r') as f:
        adap_data = json.load(f)
        
    # 3. Define target network scale dimensions (N)
    dimensions = [11, 50, 100, 500, 1000, 5000]
    str_dims = [str(d) for d in dimensions]
    
    try:
        # Extract Standard Baseline Loops at control configuration alpha = 0.85
        standard_spider_trap = [std_data["spider_trap"][dim]["0.85"] for dim in str_dims]
        standard_star_graph  = [std_data["star_graph"][dim]["0.85"] for dim in str_dims]
        
        # Extract Adaptive Engine Loops from the correct nested fields
        adaptive_source = adap_data.get("adaptive_core", adap_data)
        adaptive_spider_trap = [adaptive_source["spider_trap"][dim]["convergence_loops"] for dim in str_dims]
        adaptive_star_graph  = [adaptive_source["star_graph"][dim]["convergence_loops"] for dim in str_dims]
        
    except KeyError as err:
        print(f"❌ STRUCTURAL PARSING FAILURE: Missing coordinate field array key: {err}")
        print("Please check that your running engines output both topologies exactly as shown in the data files.")
        sys.exit(1)

    # 4. Print out a raw text matrix grid to verify numbers match Table II in your paper
    print("\n==================================================================")
    print("                    NUMERICAL REPLICATION MATRIX CHECK            ")
    print("==================================================================")
    print(f"{'Nodes (N)':<12}{'Std Spider':<14}{'Adap Spider':<14}{'Std Star':<12}{'Adap Star':<12}")
    for i, dim in enumerate(dimensions):
        print(f"{dim:<12}{standard_spider_trap[i]:<14}{adaptive_spider_trap[i]:<14}{standard_star_graph[i]:<12}{adaptive_star_graph[i]:<12}")
    print("==================================================================\n")

    # 5. Initialize publication-quality matplotlib layout properties
    plt.figure(figsize=(7, 5.5))
    plt.rc('font', family='serif') 
    plt.grid(True, which="both", linestyle="--", alpha=0.5)

    # Plot lines with corresponding marker tokens precisely matching your legacy manuscript design
    plt.plot(dimensions, adaptive_star_graph, marker='o', color='#1f77b4', linestyle='-', linewidth=1.2, markersize=4, label='Central Playmaker Hub (Adaptive)')
    plt.plot(dimensions, standard_star_graph, marker='s', color='#ff7f0e', linestyle='--', linewidth=1.2, markersize=4, label='Central Playmaker Hub (Standard)')
    plt.plot(dimensions, adaptive_spider_trap, marker='^', color='#2ca02c', linestyle='-', linewidth=1.2, markersize=4, label='Cyclic Defensive Loop (Adaptive)')
    plt.plot(dimensions, standard_spider_trap, marker='x', color='#d62728', linestyle='--', linewidth=1.2, markersize=4, label='Cyclic Defensive Loop (Standard)')

    # Axis constraints alignment
    plt.xscale('log')
    plt.xticks(dimensions, labels=[str(x) for x in dimensions])
    plt.xlabel('Network Structural Dimension Scale (Nodes, N)', fontsize=10, labelpad=8)
    plt.ylabel('Algorithmic Convergence Iterations (Loops)', fontsize=10, labelpad=8)
    plt.xlim(10, 6000)
    plt.ylim(20, 110)
    plt.legend(loc='lower left', frameon=True, fontsize=8, facecolor='white', edgecolor='#e0e0e0')
    plt.tight_layout()

    # 6. Route output to requested target location vector
    target_output_file = os.path.join(output_dir, "scalability_convergence_curves.pdf")
    plt.savefig(target_output_file, format='pdf', dpi=300)
    plt.close()
    
    print(f"🎉 PLOT SUCCESS: Figure 1 curve successfully compiled from data logs.")
    print(f"Target Output Path: {target_output_file}\n")

if __name__ == "__main__":
    main()
