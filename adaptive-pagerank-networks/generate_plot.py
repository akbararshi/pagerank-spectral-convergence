import os
import matplotlib.pyplot as plt

# 1. Direct Target Directory Initialization (Points straight to main output folder)
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# 2. Synchronized Data Arrays (Matching your production JSON logs)
nodes = ['11', '50', '100', '500', '1000', '5000']
x_indices = range(len(nodes))

# Central Playmaker Hub (Star Topology)
star_adaptive = [84, 89, 89, 89, 89, 89]
star_standard = [89, 90, 90, 90, 90, 90]

# Cyclic Defensive Loop (Spider-Trap Topology)
spider_adaptive = [74, 49, 61, 51, 47, 37]
spider_standard = [75, 49, 61, 52, 47, 37]

# 3. Figure Geometry & Canvas Setup
plt.figure(figsize=(7.5, 5.5))
ax = plt.gca()

# 4. Plotting Trajectories with Exact Specification Matching
plt.plot(x_indices, star_adaptive, label='Central Playmaker Hub (Adaptive)', 
         color='#1f77b4', linestyle='-', marker='o', markersize=5, linewidth=1.2)
plt.plot(x_indices, star_standard, label='Central Playmaker Hub (Standard)', 
         color='#ff7f0e', linestyle='--', marker='s', markersize=5, linewidth=1.2)
plt.plot(x_indices, spider_adaptive, label='Cyclic Defensive Loop (Adaptive)', 
         color='#2ca02c', linestyle='-', marker='^', markersize=5, linewidth=1.2)
plt.plot(x_indices, spider_standard, label='Cyclic Defensive Loop (Standard)', 
         color='#d62728', linestyle='--', marker='x', markersize=6, linewidth=1.2)

# 5. Axes Limits and Categorical Tick Labeling
plt.xticks(x_indices, nodes)
plt.xlim(-0.2, len(nodes) - 0.8)
plt.ylim(20, 110)
plt.yticks(range(20, 111, 10))

# 6. Professional Typography & Layout Formatting
plt.xlabel('Network Structural Dimension Scale (Nodes, N)', fontsize=10, labelpad=8)
plt.ylabel('Algorithmic Convergence Iterations (Loops)', fontsize=10, labelpad=8)
plt.tick_params(axis='both', which='major', labelsize=9, direction='in', top=True, right=True)

# 7. Gridline and Legend Architecture
plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='#cbd5e1')
plt.legend(loc='lower left', frameon=True, facecolor='white', framealpha=0.9, 
           edgecolor='#e2e8f0', fontsize=8.5, labelspacing=0.4)

# 8. Vector PDF Render and Save Setup
plt.tight_layout()
output_path = os.path.join(output_dir, 'scalability_convergence_curves.pdf')
plt.savefig(output_path, bbox_inches='tight', format='pdf')
plt.close()

print(f"Success: Vector quality PDF chart overwritten straight to: {output_path}")

    
import os
import json
import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def plot_barcelona_passing_network():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_folder = os.path.join(current_dir, 'output')
    results_path = os.path.join(output_folder, 'football_experimental_results.json')
    plot_output_path = os.path.join(output_folder, 'barca_passing_network.pdf')

    # 1. Load adaptive influence scores from your output payload
    if not os.path.exists(results_path):
        print(f"[ERROR] Source metric vector file not found at: {results_path}")
        return
        
    with open(results_path, 'r', encoding='utf-8') as f:
        experimental_results = json.load(f)
        
    barca_scores = experimental_results.get("2011_UCL_Final", {})

    player_mapping = {
        "víctor valdés arribas": "Valdés",
        "daniel alves da silva": "Dani Alves",
        "gerard piqué bernabéu": "Piqué",
        "javier alejandro mascherano": "Mascherano",
        "eric-sylvain bilal abidal": "Abidal",
        "sergio busquets i burgos": "Busquets",
        "xavier hernández creus": "Xavi",
        "andrés iniesta luján": "Iniesta",
        "pedro eliezer rodríguez ledesma": "Pedro",
        "david villa sánchez": "Villa",
        "lionel andrés messi cuccittini": "Messi"
    }

    tactical_positions = {
        "Valdés": (40.0, 8.0),
        "Dani Alves": (72.0, 34.0),
        "Piqué": (53.0, 24.0),
        "Mascherano": (27.0, 24.0),
        "Abidal": (8.0, 34.0),
        "Busquets": (40.0, 46.0),
        "Xavi": (55.0, 68.0),
        "Iniesta": (25.0, 68.0),
        "Messi": (40.0, 84.0),  
        "Pedro": (66.0, 102.0),
        "Villa": (14.0, 102.0)
    }

    # 2. Ingest spatial event-stream coordinates via the StatsBomb data repository
    try:
        from statsbombpy import sb
    except ImportError:
        os.system('pip install statsbombpy pandas matplotlib networkx')
        from statsbombpy import sb

    match_id = 18236
    team_name = "Barcelona"
    print(f"[Visual Pipeline] Extracting spatial tracking matrices for Match ID: {match_id}")
    events_df = sb.events(match_id=match_id)
    
    pass_mask = (
        (events_df['type'] == 'Pass') &
        (events_df['team'] == team_name) &
        (events_df['pass_outcome'].isna()) &
        (~events_df['pass_type'].isin(['Corner', 'Free Kick', 'Throw-in', 'Kick Off']))
    )
    filtered_passes = events_df[pass_mask]
    sb_unique_players = filtered_passes['player'].dropna().unique()

    sb_to_clean = {}
    for sb_name in sb_unique_players:
        sb_low = sb_name.lower()
        for raw_key, clean_name in player_mapping.items():
            raw_low = raw_key.lower()
            if raw_low in sb_low or sb_low in raw_low:
                sb_to_clean[sb_name] = clean_name
                break

    # 3. Construct Undirected Graph and Track Metrics
    G = nx.Graph()  
    mvp_player = None
    max_dependency = -1.0

    for raw_key, clean_name in player_mapping.items():
        metrics = barca_scores.get(raw_key, {})
        if not metrics:
            for k, v in barca_scores.items():
                if clean_name.lower() in k.lower() or k.lower() in raw_key:
                    metrics = v
                    break
        
        node_weight = metrics.get("adaptive_score", 0.0909)
        dep_score = metrics.get("dependency_score", 0.0)
        
        if dep_score > max_dependency:
            max_dependency = dep_score
            mvp_player = clean_name
            
        G.add_node(clean_name, weight=node_weight, dependency=dep_score, pos=tactical_positions[clean_name])

    pair_counts = {}
    for _, row in filtered_passes.iterrows():
        src_sb = row['player']
        dst_sb = row.get('pass_recipient')
        src_clean = sb_to_clean.get(src_sb)
        dst_clean = sb_to_clean.get(dst_sb)
            
        if src_clean and dst_clean and src_clean in tactical_positions and dst_clean in tactical_positions:
            if src_clean != dst_clean:
                sorted_pair = tuple(sorted([src_clean, dst_clean]))
                pair_counts[sorted_pair] = pair_counts.get(sorted_pair, 0) + 1

    # Filter out low-frequency noise pairs to keep layout clean
    for (node_a, node_b), combined_count in pair_counts.items():
        if combined_count >= 15:  
            G.add_edge(node_a, node_b, weight=combined_count)

    # 4. Vibrant Canvas Layout Configurations (X: 0-80, Y: 0-120)
    fig, ax = plt.subplots(figsize=(8, 11), dpi=300)
    ax.set_facecolor('#0b2416')  
    fig.patch.set_facecolor('#0f2415')

    # Draw sharp white tactical pitch markings
    plt.plot([0, 80, 80, 0, 0], [0, 0, 120, 120, 0], color="#ffffff", lw=2.5, alpha=0.9)
    plt.plot([0, 80], [60, 60], color="#ffffff", lw=2.5, alpha=0.9)
    
    center_circle = patches.Circle((40, 60), 9.15, edgecolor="#ffffff", facecolor="none", lw=2.5, alpha=0.9)
    ax.add_patch(center_circle)
    plt.scatter(40, 60, color="#ffffff", s=20, alpha=0.9)

    # Penalty box outlines
    ax.add_patch(patches.Rectangle((18, 0), 44, 16.5, edgecolor="#ffffff", facecolor="none", lw=2.5, alpha=0.9))
    ax.add_patch(patches.Rectangle((18, 103.5), 44, 16.5, edgecolor="#ffffff", facecolor="none", lw=2.5, alpha=0.9))
    ax.add_patch(patches.Rectangle((30, 0), 20, 5.5, edgecolor="#ffffff", facecolor="none", lw=1.5, alpha=0.6))
    ax.add_patch(patches.Rectangle((30, 114.5), 20, 5.5, edgecolor="#ffffff", facecolor="none", lw=1.5, alpha=0.6))

    node_positions = nx.get_node_attributes(G, 'pos')
    
    # 5. Render Clean Single Prominent Passing Lanes (Refined Line Width Multiplier)
    for edge in G.edges():
        pass_volume = G.edges[edge]['weight']
        
        # DOWNGRADED MULTIPLIER: Dropped from 0.20 to 0.12 to thin out the lines elegantly
        w = 1.0 + (pass_volume - 15) * 0.12
        line_alpha = min(0.35 + (pass_volume * 0.007), 0.85)
        
        nx.draw_networkx_edges(
            G, node_positions, edgelist=[edge], width=w,
            edge_color='#ffffff', alpha=line_alpha,
            connectionstyle='arc3,rad=0.0'
        )
    
    # 6. Render Nodes with Golden Ring for the MVP (Refined Node Sizes Scaling Factor)
    for node in G.nodes():
        pos = node_positions[node]
        # DOWNGRADED BASE SCALE: Shifted from 25000 down to 17000 to reduce node radius
        size = G.nodes[node]['weight'] * 17000
        
        if node == mvp_player:
            nx.draw_networkx_nodes(
                G, node_positions, nodelist=[node], node_size=size * 1.05,
                node_color='#0b192e', edgecolors='#ffdf00', linewidths=3.5, alpha=1.0
            )
        else:
            nx.draw_networkx_nodes(
                G, node_positions, nodelist=[node], node_size=size,
                node_color='#0d2342', edgecolors='#cba135', linewidths=1.8, alpha=0.9
            )
    
    # 7. High-Contrast Text Labels Overlay
    for player, (x, y) in node_positions.items():
        is_mvp = (player == mvp_player)
        lbl_text = f"{player} (MVP)" if is_mvp else player
        text_color = '#ffdf00' if is_mvp else 'white'
        
        # Position label offset adjusted down slightly to align with the smaller nodes
        plt.text(
            x, y - 4.2, lbl_text, fontsize=9.0, fontweight='bold',
            color=text_color, ha='center', va='center',
            bbox=dict(facecolor='#0b2416', edgecolor='none', boxstyle='round,pad=0.2', alpha=0.8)
        )

    plt.title("FC Barcelona Structural Passing Topology\n(Dynamic Governor Mapping — 2011 UCL Final)", 
              fontsize=12, fontweight='bold', pad=15, color='white')
    plt.xlim(-4, 84)
    plt.ylim(-4, 124)
    plt.axis('off')
    
    os.makedirs(output_folder, exist_ok=True)
    plt.savefig(plot_output_path, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none', format='pdf')
    print(f"\n[SUCCESS] Refined undirected vertical network infographic written to: {plot_output_path}\n")

if __name__ == "__main__":
    plot_barcelona_passing_network()
