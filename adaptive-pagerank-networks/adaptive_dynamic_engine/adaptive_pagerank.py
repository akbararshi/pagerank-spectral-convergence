import numpy as np
import math

def calculate_graph_density(nodes_count, connection_graph):
    """
    Computes global structural edge density (rho) across a generic network map.
    Maps to Equation 5 in the research manuscript.
    """
    total_possible_edges = nodes_count * (nodes_count - 1)
    if total_possible_edges <= 0:
        return 0.0
        
    # Count unique active directed edge allocations present in the adjacency mapping
    active_edges = sum(len(neighbors) for neighbors in connection_graph.values())
    return float(active_edges) / total_possible_edges

def macroscopic_sigmoid_governor(density):
    """
    Routes global edge density through a logistic sigmoid curve.
    Maps to Equation 6 in the research manuscript.
    """
    exponent_delta = -10.0 * (density - 0.45)
    # Protection vector against numerical float underflow/overflow
    exponent_delta = max(-50.0, min(50.0, exponent_delta))
    denominator = 1.0 + math.exp(exponent_delta)
    return 0.85 + (0.13 / denominator)

def run_adaptive_power_iteration(nodes_count, connection_graph, max_loops=2000, precision=1e-6):
    """
    Executes raw row-stochastic power iteration using the dynamic sigmoid governor.
    Operates over generic graph networks independent of sports metrics.
    
    Returns:
        stationary_distribution (list): Calculated node ranks.
        iterations_run (int): Final loop count to hit tolerance ceiling.
        density (float): Structural network edge density.
        dynamic_alpha (float): Computed damping coefficient.
    """
    # 1. Compute density and pull dynamic parameter limits from the sigmoid engine
    density = calculate_graph_density(nodes_count, connection_graph)
    dynamic_alpha = macroscopic_sigmoid_governor(density)
    
    # 2. Set up row vector allocations (1 x N array structures)
    vector_p = np.ones(nodes_count, dtype=float) / nodes_count
    
    # Build out-degree reference array to capture outbound row weights
    out_degrees = np.zeros(nodes_count, dtype=float)
    for src, targets in connection_graph.items():
        if src < nodes_count:
            out_degrees[src] = len(targets)
            
    # Track non-dangling vs structural matrix sinks
    is_dangling = (out_degrees == 0)
    
    # 3. Core power iteration sequence loop
    iterations_run = 0
    
    for cycle in range(max_loops):
        next_vector_p = np.zeros(nodes_count, dtype=float)
        
        # Calculate trailing dangling mass to handle column traps cleanly
        dangling_mass = np.sum(vector_p[is_dangling]) / nodes_count
        
        # Distribute ranks through active connection channels
        for src in range(nodes_count):
            if not is_dangling[src] and vector_p[src] > 0:
                allocated_rank = vector_p[src] / out_degrees[src]
                for target in connection_graph[src]:
                    if target < nodes_count:
                        next_vector_p[target] += allocated_rank
                        
        # Combine structural transitions, dangling redistribution, and teleportation bounds
        teleport_mass = (1.0 - dynamic_alpha) / nodes_count
        next_vector_p = (dynamic_alpha * (next_vector_p + dangling_mass)) + teleport_mass
        
        # Compute L1 norm convergence delta check
        error = np.sum(np.abs(next_vector_p - vector_p))
        
        vector_p = next_vector_p
        iterations_run = cycle + 1
        
        if error < precision:
            break
            
    return vector_p.tolist(), iterations_run, density, dynamic_alpha
