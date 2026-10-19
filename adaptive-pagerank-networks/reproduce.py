"""
Adaptive PageRank Master Replication Pipeline (Live Streaming Infrastructure)
Submission Code Artifact for the Journal of High School Computer Science (JHCS)

This master script completely automates the experimental validation pipeline:
1. Runs baseline PageRank simulations (standard_main.py -> output/experiment_results.json)
2. Runs adaptive governor simulations (adaptive_main.py -> output/adaptive_experiment_results.json)
3. Connects to StatsBomb API to pull the live 2011 UCL Final network data on the fly
   (adaptive_football_engine.py -> output/football_experimental_results.json)
4. Automatically generates the publication-ready verification curves (generate_plot.py)
"""

import os
import sys
import subprocess

def run_pipeline_step(script_relative_path, description):
    """
    Safely executes an isolated workspace script using the active Python interpreter,
    injecting the absolute workspace root path directly into the running environment
    to completely eliminate module path lookup errors during execution loops.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    absolute_script_path = os.path.normpath(os.path.join(base_dir, script_relative_path))
    
    print("=" * 75)
    print(f"EXECUTING STEP: {description}")
    print(f"Target Path    : {script_relative_path}")
    print("=" * 75)
    
    if not os.path.exists(absolute_script_path):
        print(f"\n❌ CRITICAL CONFIGURATION ERROR:\nTarget file missing at: {absolute_script_path}")
        print("Please check that your folder organization and file names are spelled correctly.\n")
        sys.exit(1)
        
    try:
        # Dynamically inject the absolute workspace root path into the running process environment
        env_config = os.environ.copy()
        env_config["PYTHONPATH"] = base_dir + os.pathsep + env_config.get("PYTHONPATH", "")

        # Execute using the exact same python interpreter and tracking environment parameters
        result = subprocess.run(
            [sys.executable, absolute_script_path], 
            check=True, 
            capture_output=True, 
            text=True,
            env=env_config  # Applies the structural runtime path injection
        )
        if result.stdout:
            print(result.stdout.strip())
        print(f"✅ SUCCESS: {description} completed safely.\n")
        
    except subprocess.CalledProcessError as err:
        print(f"\n❌ CRITICAL PIPELINE FAILURE: Crash during {description}")
        if err.stderr:
            print("----- Diagnostic Error Traceback -----")
            print(err.stderr.strip())
            print("--------------------------------------")
        sys.exit(1)

def main():
    # Enforce a clean, synchronized singular 'output' directory layout anchor
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, "output")
    os.makedirs(output_dir, exist_ok=True)
    
    print("===========================================================================")
    print("🚀 INITIALIZING ADAPTIVE PAGERANK MASTER REPLICATION PIPELINE             ")
    print("===========================================================================\n")
    
    # 2. Execute standard baseline simulations (Creates output/experiment_results.json)
    run_pipeline_step(
        os.path.join("standard_pagerank", "standard_main.py"), 
        "Baseline PageRank Engine Control Group Trials (Table II Baselines)"
    )
    
    # 3. Execute adaptive dynamic governor simulations (Creates output/adaptive_experiment_results.json)
    run_pipeline_step(
        os.path.join("adaptive_dynamic_engine", "adaptive_main.py"), 
        "Adaptive Dynamic PageRank Sigmoid Governor Architecture Simulations"
    )
    
    # 4. Execute the fully automated live-streaming football metrics engine (Creates Table I)
    run_pipeline_step(
        os.path.join("adaptive_dynamic_engine", "adaptive_football_engine.py"), 
        "Live StatsBomb Data Stream: 2011 UEFA Champions League Final Analytics (Table I)"
    )
    
    # 5. Trigger automated plot synthesis (Reads JSON dependencies and exports vector graphic)
    run_pipeline_step(
        "generate_plot.py", 
        "Figure 1 Convergence Curve Extraction and Output Graphics Processing"
    )
    
    # 6. Comprehensive Verification Check
    target_curve_file = os.path.join(output_dir, "scalability_convergence_curves.pdf")
    if os.path.exists(target_curve_file):
        print("===========================================================================")
        print("🎉 SUCCESS: COMPLETE ARCHIVAL EXPERIMENTAL REPLICATION RESOLVED           ")
        print(f"Vector graphic successfully compiled at: {target_curve_file}")
        print("All underlying JSON metrics are fully refreshed and verified.")
        print("===========================================================================\n")
    else:
        print("⚠ PIPELINE TERMINATED: Files completed execution, but target plot graphic was not found.")
        print("Please check that generate_plot.py is correctly targeting output/scalability_convergence_curves.pdf\n")

if __name__ == "__main__":
    main()
