import os
import sys
import subprocess

def run_script(script_path, description):
    print("=" * 80)
    print(f"🚀 RUNNING: {description}")
    print(f"📁 Path: {script_path}")
    print("=" * 80)
    
    if not os.path.exists(script_path):
        print(f"❌ ERROR: Script not found at {script_path}\n", file=sys.stderr)
        return False

    script_dir = os.path.dirname(script_path)
    script_name = os.path.basename(script_path)
    
    try:
        original_cwd = os.getcwd()
        if script_dir:
            os.chdir(script_dir)
            
        process = subprocess.Popen(
            [sys.executable, script_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )
        
        for line in process.stdout:
            print(line, end="")
            
        process.wait()
        os.chdir(original_cwd)
        
        if process.returncode == 0:
            print(f"\n✅ SUCCESS: {description} completed cleanly.\n")
            return True
        else:
            print(f"\n❌ FAILURE: {description} exited with error code {process.returncode}\n", file=sys.stderr)
            return False
            
    except Exception as e:
        print(f"\n❌ EXCEPTION occurred while running {description}: {str(e)}\n", file=sys.stderr)
        return False

def main():
    print("🌟 STARTING ADAPTIVE PAGERANK REPRODUCTION PIPELINE 🌟\n")
    
    pipeline_steps = [
        ("football_experimental_results.py", "Football Real-Match Baseline Analysis"),
        ("adaptive_dynamic_engine/adaptive_main.py", "Adaptive Damping Engine Verification Loop"),
        ("standard_pagerank/standard_main.py", "Standard Static PageRank Control Run"),
        ("generate_plot.py", "Synthetic 5,000-Node Scalability Convergence Visualization Generation")
    ]
    
    pipeline_success = True
    for script, desc in pipeline_steps:
        success = run_script(script, desc)
        if not success:
            pipeline_success = False
            print("⚠️ Pipeline interrupted or met error anomalies. Halting step cascade.")
            break
            
    if pipeline_success:
        print("=" * 80)
        print("🎉 ALL REPRODUCTION TASKS EXECUTED PERFECTLY 🎉")
        print("📝 Outputs successfully saved to their respective directories.")
        print("=" * 80)

if __name__ == "__main__":
    main()
