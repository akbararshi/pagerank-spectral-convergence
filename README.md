# Beyond 0.85: Adaptive PageRank Architecture for Multi-Agent Flow Networks
Developed by **Akbar Arshi**

## 🚀 Executive Summary
Traditional graph algorithms (like Google’s baseline PageRank) fail when scaled down to dense, multi-agent sports environments because they suffer from **possession-recycling bias**. They mistake safe, low-risk horizontal passing loops along a defensive backline for true structural prestige. This misallocates mathematical importance away from high-impact vertical playmakers operating in contested central zones.

To solve this, I designed and engineered an **Adaptive Dynamic PageRank Architecture**. My framework introduces a **Macroscopic Sigmoid Governor** to scale teleportation thresholds dynamically based on real-time edge density, paired with an **Absolute Outbound Volume Weighting Matrix** to isolate true playmaker hubs. Tested against empirical open-play event streams (StatsBomb dataset) from the 2011 UEFA Champions League Final, this model successfully isolated the team's mastermind nucleus, backed by a modified **Floyd-Warshall node-deletion sequence** proving structural dependency polarity.

---

## 🛠️ Project Core Blueprint
* **Core Innovation:** Formulated a localized logistic decay ceiling (\(D_{\text{global}}\) ranging smoothly from 0.85 up to 0.98) to suppress random walk teleportation leaks.
* **Engineering & Scalability:** Built synthetic graph topologies to stress-test the model's numerical stability up to **N = 5,000 nodes**.
* **Interdisciplinary Vision:** Bridged sports network redundancy models directly into **network neuroscience** to simulate targeted network collapse configurations in Alzheimer's disease connectomes.
* **Technical Stack:** Python, NetworkX, NumPy, Pandas, SciPy, Matplotlib, StatsBombPy API.

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

```text
pagerank-spectral-convergence/             <-- Main Workspace Root
├── .gitignore                             <-- Git environment exclusion rules
├── README.md                              <-- Replication documentation
├── requirements.txt                       <-- Python environment requirements
└── adaptive-pagerank-networks/            <-- Project Core Directory
    ├── adaptive_dynamic_engine/
    │   ├── adaptive_football_engine.py    <-- Runs adaptive damping engine for football scenarios
    │   ├── adaptive_main.py                   
    │   └── adaptive_pagerank.py           <-- Core adaptive pagerank logic
    ├── output/                            <-- Analytical payload dumps
    │   ├── adaptive_experiment_results.json   
    │   ├── experiment_results.json            
    │   ├── football_experimental_results.json 
    │   ├── scalability_convergence_curves.pdf 
    │   └── simple_graphs.py                   <-- Synthetic topological loop graphs
    ├── standard_pagerank/
    │   ├── standard_main.py                   
    │   └── standard_pagerank_engine.py    <-- Core baseline pagerank code
    ├── football_experimental_results.py       
    ├── generate_plot.py                       
    └── reproduce.py                       <-- Master runtime orchestrator script

```

---

## Replication and Execution

To execute the entire simulation matrix, verify system convergence parameters, and regenerate all analytical graph assets from scratch, navigate into the core subdirectory and trigger the orchestrator:

```bash
cd adaptive-pagerank-networks
python reproduce.py
```

---

## System Processing Workflow

1. **Console Allocation Tables:** The script builds adjacent passing matrices using public 2011 UEFA Champions League dataset streams and prints comparative baseline tables.
2. **Dynamic Data Tracking:** The system solves the Sigmoid Governor bounds, outputting player shares and dependency rankings directly to `output/football_experimental_results.json`.
3. **Visualization Generation:** The script triggers the visualization layout layer, exporting performance scalability tracking data to `output/scalability_convergence_curves.pdf`.

## 🛠️ Reproducibility & Tool Disclosure

This repository contains the complete implementation and replication scripts for the associated research paper. 

### Generative AI Use
* **Scope:** Generative AI tools were utilized strictly for structural scaffolding and workflow optimization within the data orchestration layer.
* **Target Scripts:** The utility script `generate_plot.py` handles input parsing, OS path validation (`os.path.join`), and initial graph configurations via `matplotlib.pyplot`. These non-analytical operations were assisted by AI to facilitate automated pipeline testing.
* **Verification:** Every logical construct, exception threshold, and layout output was audited, refactored, and execution-verified by the author. The data processing and analysis results presented in the manuscript are entirely determined by the custom code logic.

