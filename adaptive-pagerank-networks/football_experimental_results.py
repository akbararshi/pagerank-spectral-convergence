import os
import sys
import numpy as np
import pandas as pd
import json

# ==============================================================================
# 1. GRAPH SYSTEM LAYER ENVIRONMENT SETUP
# ==============================================================================
current_dir = os.path.dirname(os.path.abspath(__file__))
adaptive_folder = os.path.join(current_dir, 'adaptive_dynamic_engine')
standard_folder = os.path.join(current_dir, 'standard_pagerank')
output_folder = os.path.join(current_dir, 'output')

os.makedirs(output_folder, exist_ok=True)

sys.path.append(adaptive_folder)
sys.path.append(standard_folder)

# Hardcoded module tracking based on explicit repository configuration parameters
try:
    from standard_pagerank.standard_pagerank_engine import run_matrix_power_iteration
    from adaptive_dynamic_engine.adaptive_football_engine import adaptive_pagerank, system_dependency
except ImportError as path_exception:
    print(f"\n[PATH ERROR] Initialization aborted. Unable to load core engines: {path_exception}")
    sys.exit(1)

# ==============================================================================
# 2. SELECTIONS EVENT STREAM EXTRACTION INTERFACE
# ==============================================================================
def load_match_via_statsbombpy(match_id=18236, team_name="Barcelona"):
    try:
        from statsbombpy import sb
    except ImportError:
        print("\n[ENVIRONMENT NOTICE] Executing package validation: pip install statsbombpy")
        os.system('pip install statsbombpy pandas')
        from statsbombpy import sb

    print(f"\n[Client Datastream Engine] Fetching event records for Match ID: {match_id}")
    events_df = sb.events(match_id=match_id)
    
    unique_teams = events_df['team'].dropna().unique()
    if team_name not in unique_teams:
        for team_entry in unique_teams:
            if team_name.lower() in team_entry.lower() or team_entry.lower() in team_name.lower():
                print(f"  [System Correction] Aligned parameter entry '{team_name}' with relational record: '{team_entry}'")
                team_name = team_entry
                break
                
    pass_mask = (
        (events_df['type'] == 'Pass') &
        (events_df['team'] == team_name) &
        (events_df['pass_outcome'].isna()) &
        (~events_df['pass_type'].isin(['Corner', 'Free Kick', 'Throw-in', 'Kick Off']))
    )
    filtered_passes = events_df[pass_mask]
    
    player_counts = events_df[events_df['team'] == team_name]['player'].value_counts()
    top_11_players = list(player_counts.index[:11])
    
    if len(top_11_players) == 0:
        top_11_players = list(events_df[events_df['team'] == team_name]['player'].dropna().unique()[:11])
        
    player_to_idx = {name: idx for idx, name in enumerate(top_11_players)}
    
    passing_matrix = np.zeros((11, 11), dtype=float)
    for _, row in filtered_passes.iterrows():
        src_player = row['player']
        rcp_player = row.get('pass_recipient')
        if src_player in player_to_idx and rcp_player in player_to_idx:
            passing_matrix[player_to_idx[src_player], player_to_idx[rcp_player]] += 1
            
    return top_11_players, passing_matrix

# ==============================================================================
# 3. DATA PURIFICATION UTILITIES
# ==============================================================================
def absolute_clean_payload(obj):
    """Recursively processes specific hexadecimal anomalies and decodes standard string sequences."""
    if isinstance(obj, dict):
        return {absolute_clean_payload(k): absolute_clean_payload(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [absolute_clean_payload(elem) for elem in obj]
    elif isinstance(obj, str):
        obj = obj.replace(r"\u00e11", r"\u00e1").replace(r"\u00e99", r"\u00e9")
        obj = obj.replace(r"\u00ed1", r"\u00ed").replace(r"\u00fa1", r"\u00fa")
        try:
            return obj.encode('utf-8').decode('unicode_escape')
        except Exception:
            return obj
    return obj
# ==============================================================================
# 4. MULTI-ENVIRONMENT VALIDATION LOOP EXECUTION (SELF-CONTAINED DATA INGEST)
# ==============================================================================
if __name__ == "__main__":
    import networkx as nx

    MATCH_SUITE = {
        "2011_UCL_Final":    {"match_id": 18236,   "team": "Barcelona"},
        "2022_WC_Morocco":   {"match_id": 3869486, "team": "Morocco"},
        "2022_WC_Argentina": {"match_id": 3869685, "team": "Argentina"}
    }

    multi_match_payload = {}

    for match_key, config in MATCH_SUITE.items():
        print(f"\n[EVALUATION PROCESS] Simulating structural graph matrix for: {match_key} ({config['team']})")
        
        roster, raw_matrix = load_match_via_statsbombpy(match_id=config["match_id"], team_name=config["team"])
        N = len(roster)

        if N == 0:
            print(f"  [ERROR] Terminating evaluation trace for {config['team']}. Sample allocation failed.")
            continue

        duration_mapping = {
            "2011_UCL_Final": 95.0,
            "2022_WC_Morocco": 102.0,
            "2022_WC_Argentina": 140.0
        }
        active_minutes = duration_mapping.get(match_key, 90.0)

        normalized_matrix = (raw_matrix / active_minutes) * 90.0
        filtered_matrix = np.where(normalized_matrix >= 2.0, raw_matrix, 0)

        active_edges = np.count_nonzero(filtered_matrix)
        max_possible_edges = N * (N - 1)
        calculated_density = float(active_edges) / float(max_possible_edges) if max_possible_edges > 0 else 0.0

        calculated_damping = 0.50 + (0.35 / (1.0 + np.exp(12.0 * (calculated_density - 0.50))))


        # 2. BASELINE CONTROL SPECIFICATION: UNWEIGHTED STRUCTURAL MAPPING
        connection_graph = {}
        for i in range(N):
            unique_targets = [j for j in range(N) if raw_matrix[i][j] > 0]
            connection_graph[i] = unique_targets

        standard_scores, execution_cycles = run_matrix_power_iteration(
            nodes_count=N, 
            connection_graph=connection_graph, 
            damping_coeff=0.85, 
            max_loops=2000, 
            precision=1e-6
        )
        
        # 3. PROPOSED SOLUTION SPECIFICATION: ADAPTIVE ALGORITHMIC PROCESSING
        adaptive_output = adaptive_pagerank(filtered_matrix, roster, active_minutes=active_minutes)
        dependency_output = system_dependency(raw_matrix, roster)

        # Safely extract scores vector regardless of returned tuple length
        if isinstance(adaptive_output, tuple) and len(adaptive_output) > 0:
            v2_scores = adaptive_output[0]
        else:
            v2_scores = adaptive_output

        if isinstance(dependency_output, tuple) and len(dependency_output) > 0:
            final_dependency_map = dependency_output[0]
        else:
            final_dependency_map = dependency_output
        
        # 4. COMPETING INVARIANTS FRAMEWORK: COMPARATIVE TOPOLOGY MODELING
        G = nx.DiGraph()
        for i in range(N):
            for j in range(N):
                if raw_matrix[i][j] > 0 and i != j:
                    G.add_edge(roster[i], roster[j], weight=raw_matrix[i][j], distance=1.0 / raw_matrix[i][j])
        
        betweenness_dict = nx.betweenness_centrality(G, weight='distance', normalized=True)
        
        try:
            eigenvector_dict = nx.eigenvector_centrality(G, weight='weight', max_iter=2000, tol=1e-4)
        except nx.PowerIterationFailedConvergence:
            eigenvector_dict = nx.degree_centrality(G)

        # 5. ASSEMBLE FLAT PLAYER-KEYED LAYOUT WITH GLOBAL METADATA BLOCK
        match_dictionary = {}
        
        match_dictionary["metadata"] = {
            "edge_density": round(calculated_density, 4),
            "calculated_damping_factor": round(calculated_damping, 4)
        }

        for i in range(N):
            p_name = roster[i]
            
            if hasattr(final_dependency_map, 'get'):
                dep_score = final_dependency_map.get(p_name, 0.0)
            elif isinstance(final_dependency_map, (list, np.ndarray, tuple)):
                dep_score = final_dependency_map[i]
            else:
                dep_score = 0.0

            match_dictionary[p_name] = {
                "standard_share": float(standard_scores[i]),
                "adaptive_score": float(v2_scores[i]),
                "dependency_score": float(dep_score),
                "betweenness_score": float(betweenness_dict.get(p_name, 0.0)),
                "eigenvector_score": float(eigenvector_dict.get(p_name, 0.0))
            }
        
        multi_match_payload[match_key] = match_dictionary
        print(f"\n--- FORCE VERIFICATION FOR {match_key} ---")
        print(f"Current Density: {calculated_density:.4f}")
        print(f"Resulting Damping: {calculated_damping:.4f}")
        
    # 6. SERIALIZATION AND EXPORT LAYER
    pristine_payload = absolute_clean_payload(multi_match_payload)

    export_target_path = os.path.join(output_folder, 'football_experimental_results.json')
    with open(export_target_path, 'w', encoding='utf-8') as json_out:
        json.dump(pristine_payload, json_out, indent=4, ensure_ascii=False)

    print(f"\n[SUCCESS] Consolidated multi-match benchmarking dataset written to: {export_target_path}\n")



