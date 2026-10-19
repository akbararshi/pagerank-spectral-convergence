# Beyond 0.85: Adaptive PageRank Damping Factors for Small-Scale Networks

This repository contains the official, fully reproducible implementation for the computational models presented in the accompanying manuscript. The framework evaluates dynamic scaling systems for PageRank damping factor configurations inside small-scale tactical sports networks.

The project introduces a **Macroscopic Sigmoid Governor** to dynamically adapt damping parameters between \(0.85\) and \(0.98\) based on structural graph density, counteracting possession-recycling biases in competitive team passing networks.

---

## Technical Specifications

| Dependency Component | Requirement Specification | Purpose within Pipeline |
| :--- | :--- | :--- |
| **Python Version** | Python 3.8 or higher | Base runtime environment |
| **NumPy** | Latest stable release | Matrix vector computations |
| **Pandas** | Latest stable release | Structured event frame handling |
| **SciPy** | Latest stable release | Sparse network optimizations |
| **NetworkX** | Latest stable release | Graph construction and metric extraction |
| **Matplotlib** | Latest stable release | Visual performance chart rendering |
| **StatsBombPy** | Latest stable release | Public match event stream access layer |

---

## Project Repository Architecture

The workspace layout separates core algorithm computation pipelines from outputs:

pagerank-spectral-convergence/     <-- Main Workspace Root
├── .gitignore                      <-- Git environment exclusion rules
├── README.md                       <-- Replication documentation
├── requirements.txt                <-- Python environment requirements
├── adaptive-pagerank-networks/     <-- Core framework package
│   ├── adaptive_dynamic_engine/
│   │   ├── adaptive_football_engine.py  <-- Runs adaptive damping engine applied specifically to football scenarios
│   │   ├── adaptive_main.py             <-- Uses adaptive damping engine code to output required experiment results
│   │   └── adaptive_pagerank.py         <-- The core adaptive pagerank code
│   ├── output/
│   │   ├── adaptive_experiment_results.json    <--- Adaptive pagerank experimental results
│   │   ├── experiment_results.json             <--- Standard pagerank experimental results
│   │   ├── football_experimental_results.json  <-- Real match experimental results- shows metrics such as player dependency and score in both standard and adaptive pagerank
│   │   ├── scalability_convergence_curves.pdf <-- Visual performance curves drawing comparisons between standard and proposed adaptive pagerank
│   │   └── simple_graphs.py                   <--- Cyclic defensive loop and central playmaker hub network definitions
│   ├── standard_pagerank/
│   │   ├── standard_main.py             <-- Uses standard pagerank to output desired experiment results
│   │   └── standard_pagerank_engine.py  <-- The core pagerank code
│   ├── football_experimental_results.py    <--- Runs and formats real match football experimental: Stores output in output/football_experimental_results.json
│   ├── generate_plot.py                 
│   └── reproduce.py                     <-- Master execution script
```
```

---

## Replication and Execution

To execute the entire simulation matrix, verify system convergence parameters, and regenerate all analytical graph assets from scratch, navigate to the framework folder and run the master script:

```bash
cd adaptive-pagerank-networks
python reproduce.py
```

### System Processing Workflow:
1. **Console Allocation Tables:** The script builds adjacent passing matrices using public 2011 UEFA Champions League dataset streams and prints comparative baseline tables.
2. **Dynamic Data Tracking:** The system solves the Sigmoid Governor bounds, outputting player shares and dependency rankings directly to `output/football_experimental_results.json`.
3. **Visualization Generation:** The script triggers the visualization layout layer, exporting performance scalability tracking data to `output/scalability_convergence_curves.pdf`.

---

## Double-Blind Peer Review Compliance
This workspace is structurally scrubbed of identifying information. It contains no developer names, institutional metadata, or local computer directory paths. All paths are resolved dynamically relative to the execution root.
