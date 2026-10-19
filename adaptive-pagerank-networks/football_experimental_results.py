import json
import math
import sys
import os
import numpy as np

# =========================================================================
# 1. DYNAMIC SYSTEM PATH ALLOCATOR (MODULAR DIRECTORY TREE PATHING)
# =========================================================================
current_dir = os.path.dirname(os.path.abspath(__file__))

adaptive_folder = os.path.join(current_dir, 'adaptive_dynamic_engine')
standard_folder = os.path.join(current_dir, 'standard_pagerank', 'src')
data_folder = os.path.join(current_dir, 'data')

os.makedirs(data_folder, exist_ok=True)

sys.path.append(adaptive_folder)
sys.path.append(standard_folder)

# Clean, automated module loading from your separate backend folder scopes
try:
    from standard_pagerank.standard_pagerank_engine import run_matrix_power_iteration
    from adaptive_dynamic_engine.adaptive_football_engine import adaptive_pagerank, system_dependency
except ImportError as e:
    print(f"\n[IMPORT PATH ERROR] Could not find calculation modules. Details: {e}")
    sys.exit(1)

# =========================================================================
# 2. STATSBOMBPY LIVE INTEGRATION ARCHITECTURE
# =========================================================================
def load_match_via_statsbombpy(match_id=18236, team_name="Barcelona"):
    try:
        from statsbombpy import sb
    except ImportError:
        print("\n[DEPENDENCY ERROR] Executing fallback: pip install statsbombpy")
        os.system('pip3 install statsbombpy pandas')
        from statsbombpy import sb
        
    print(f"\n[StatsBomb Client Query] Launching extraction streams for Match: {match_id}")
    events_df = sb.events(match_id=match_id)
    
    pass_mask = (
        (events_df['type'] == 'Pass') & 
        (events_df['team'] == team_name) & 
        (events_df['pass_outcome'].isna()) & 
        (~events_df['pass_type'].isin(['Corner', 'Free Kick', 'Throw-in', 'Kick Off']))
    )
    filtered_passes = events_df[pass_mask]
    
    player_counts = events_df[events_df['team'] == team_name]['player'].value_counts()
    top_11_players = list(player_counts.index[:11])
    player_to_idx = {name: idx for idx, name in enumerate(top_11_players)}
    
    passing_matrix = np.zeros((11, 11), dtype=float)
    for _, row in filtered_passes.iterrows():
        src_player = row['player']
        rcp_player = row.get('pass_recipient')
        if src_player in player_to_idx and rcp_player in player_to_idx:
            passing_matrix[player_to_idx[src_player], player_to_idx[rcp_player]] += 1
            
    return top_11_players, passing_matrix

# =========================================================================
# 3. EXPERIMENTAL PIPELINE LAYER
# =========================================================================
if __name__ == "__main__":
    roster, raw_matrix = load_match_via_statsbombpy(match_id=18236, team_name="Barcelona")
    N = len(roster)
    
    # Restructure matrix entries into standard structural dictionaries for PageRank loops
    connection_graph = {i: set() for i in range(N)}
    for i in range(N):
        for j in range(N):
            if raw_matrix[i, j] > 0:
                connection_graph[i].add(j)
                
    # --- MODEL 1 RUN (BASELINE STRIPPED TUPLE EXPANSIONS) ---
    v1_raw_output = run_matrix_power_iteration(N, connection_graph, damping_coeff=0.85)
    
    # PROBLEM FIX 1: Extract ONLY the list array index [0] if a tuple is returned
    if isinstance(v1_raw_output, tuple):
        v1_scores = v1_raw_output[0]
    else:
        v1_scores = v1_raw_output
    
    # --- MODEL 2 RUN (ADAPTIVE POWER CORE IMPORT OVERRIDES) ---
    v2_raw_dict, damping_coeff, graph_density = adaptive_pagerank(raw_matrix, roster)
    
    # PROBLEM FIX 2: Safeguard against dictionary structures returned by adaptive_pagerank
    if isinstance(v2_raw_dict, dict):
        v2_weighted = [v2_raw_dict[player] for player in roster]
    else:
        v2_weighted = v2_raw_dict
    
    # --- MODEL 3 RUN (NATIVE CALL TO YOUR EXISTING DEPENDENCY CODE) ---
    # Destructure the 3 values returned by your system_dependency file
    critical_p, peak_loss, dependency_map = system_dependency(raw_matrix, roster)
    
    # Sort ranking configurations cleanly using flat numeric lists
    v1_sort = sorted(range(N), key=lambda k: v1_scores[k], reverse=True)
    v1_ranks = {node: pos + 1 for pos, node in enumerate(v1_sort)}
    
    v2_sort = sorted(range(N), key=lambda k: v2_weighted[k], reverse=True)
    v2_ranks = {node: pos + 1 for pos, node in enumerate(v2_sort)}
    
    # Print clean presentation data table on terminal screen layout
    print("\n" + "="*122)
    print("MODULAR LAB RESULTS SUMMARY: 2011 UEFA CHAMPIONS LEAGUE FINAL EMPIRICAL CASE STUDY")
    print(f"Calculated Spatial Density: {graph_density:.4f}  |  Dynamic Sigmoid Governor Parameter: {damping_coeff:.4f}")
    print("="*122)
    print(f"{'Player Name Profile':<28} | {'V1 Centrality':<14} | {'V1 Rank':<8} | {'V2 Weighted':<14} | {'V2 Rank':<8} | {'Vulnerability (D_k)'}")
    print("-" * 122)
    for i in range(N):
        p_name = roster[i]
        print(f"{p_name:<28} | {v1_scores[i]:.4f}         | #{v1_ranks[i]:<7} | {v2_weighted[i]:<14.4f} | #{v2_ranks[i]:<7} | {dependency_map[p_name]:.4f}")
    print("="*122)
    print(f"System Structural Point-of-Failure Core Nexus Hub: {critical_p} (Total Efficiency Collapse: {peak_loss:.4f})")
    print("="*122)

    # Export compiled dataset payload to data subfolder
    payload = {
        "metadata": {"match_context": "2011 UCL Final", "density": graph_density, "governor_damping": damping_coeff},
        "results_array": []
    }
    for i in range(N):
        p_name = roster[i]
        payload["results_array"].append({
            "player": p_name, "v1_share": v1_scores[i], "v1_rank": v1_ranks[i],
            "v2_score": v2_weighted[i], "v2_rank": v2_ranks[i], "dependency": dependency_map[p_name]
        })
        
def absolute_clean_payload(obj):
    """Recursively fixes the duplicated hex typos and decodes Unicode sequences perfectly."""
    if isinstance(obj, dict):
        return {absolute_clean_payload(k): absolute_clean_payload(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [absolute_clean_payload(elem) for elem in obj]
    elif isinstance(obj, str):
        # 1. First, fix the literal duplicated number typos (\u00e11 -> \u00e1, \u00e99 -> \u00e9)
        obj = obj.replace(r"\u00e11", r"\u00e1")
        obj = obj.replace(r"\u00e99", r"\u00e9")
        
        # 2. Convert any remaining string escape slashes back into real native letters
        try:
            return obj.encode('utf-8').decode('unicode_escape')
        except Exception:
            return obj
    return obj

def absolute_clean_payload(obj):
    """Recursively fixes the duplicated hex typos and decodes Unicode sequences perfectly."""
    if isinstance(obj, dict):
        return {absolute_clean_payload(k): absolute_clean_payload(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [absolute_clean_payload(elem) for elem in obj]
    elif isinstance(obj, str):
        # 1. First, fix the literal duplicated number typos (\u00e11 -> \u00e1, \u00e99 -> \u00e9)
        obj = obj.replace(r"\u00e11", r"\u00e1")
        obj = obj.replace(r"\u00e99", r"\u00e9")
        
        # 2. Convert any remaining string escape slashes back into real native letters
        try:
            return obj.encode('utf-8').decode('unicode_escape')
        except Exception:
            return obj
    return obj

# Apply the absolute cleanup to your data structure
pristine_payload = absolute_clean_payload(payload)

# Save the perfectly clean dictionary to your file destination
export_target_path = os.path.join(data_folder, 'football_experimental_results.json')
with open(export_target_path, 'w', encoding='utf-8') as json_out:
    json.dump(pristine_payload, json_out, indent=4, ensure_ascii=False)

print(f"\n[SUCCESS] Cleaned file saved to: {export_target_path}\n")

# Apply the absolute cleanup to your data structure
pristine_payload = absolute_clean_payload(payload)

# Save the perfectly clean dictionary to your file destination
export_target_path = os.path.join(data_folder, 'football_experimental_results.json')
with open(export_target_path, 'w', encoding='utf-8') as json_out:
    json.dump(pristine_payload, json_out, indent=4, ensure_ascii=False)

print(f"\n[SUCCESS] Cleaned file saved to: {export_target_path}\n")


    