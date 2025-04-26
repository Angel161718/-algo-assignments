from itertools import permutations
import argparse
def generate_permutations(s, t):
    base = ['0'] * s + ['1'] * t
    perms = set(permutations(base))  # μοναδικές μεταθέσεις
    bin_strs = [''.join(p) for p in perms]
    index_reprs = [[i for i, bit in enumerate(b) if bit == '1'] for b in bin_strs]
    int_vals = [int(b, 2) for b in bin_strs]
    return bin_strs, index_reprs, int_vals

def hamming_distance(a, b):
    return sum(x != y for x, y in zip(a, b))

def build_graph(bin_strs):
    graph = {}
    for i, b in enumerate(bin_strs):
        graph[b] = []
        for j, other in enumerate(bin_strs):
            if i != j and hamming_distance(b, other) == 2:
                graph[b].append(other)
    return graph

def is_genlex_path(index_paths):
    for i in range(len(index_paths) - 1):
        prefix = index_paths[i]
        next_prefix = index_paths[i + 1][:len(prefix)]
        if prefix != next_prefix:
            return False
    return True
    
def hamming_index_distance(a, b):
    return sum(x != y for x, y in zip(a, b))
    
def dfs_search(path, visited, graph, idx_map, all_paths):
    if len(visited) == len(graph):
        all_paths.append(path[:])
        return
    current = path[-1]
    for neighbor in graph[current]:
        if neighbor not in visited:
            new_path = path + [neighbor]
            if is_genlex_path([idx_map[p] for p in new_path]) and hamming_index_distance(idx_map[current], idx_map[neighbor]) == 1:
                visited.add(neighbor)
                dfs_search(new_path, visited, graph, idx_map, all_paths)
                visited.remove(neighbor)
                
def find_all_dfs_paths(graph, idx_map):
    all_paths = []
    for start in graph:
        dfs_search([start], {start}, graph, idx_map, all_paths)
    return all_paths

def generate_sigma_strings(s, t):
    total = 2 ** (s - 1)
    sigmas = []
    for i in range(total):
        bits = bin(i)[2:].zfill(s - 1)
        suffix = ''.join('-' if b == '1' else '+' for b in bits)
        sigmas.append('0' * t + '-' + suffix)
    return sigmas
    
def next_bts_state(state):
    state = list(state)
    n = len(state)
    for i in range(n - 2, -1, -1):
        if i >= 1 and state[i - 1] == '0' and state[i] == '-' and state[i + 1] == '+':
            state[i - 1:i + 2] = ['-', '+', '0']
            for j in range(i + 2, n):
                if state[j] in '+-':
                    state[j] = {'+': '-', '-': '+'}[state[j]]
                    break
            return ''.join(state)
        elif i >= 1 and state[i] == '+' and state[i + 1] == '-':
            state[i:i + 2] = ['0', '+']
            for j in range(i + 2, n):
                if state[j] in '+-':
                    state[j] = {'+': '-', '-': '+'}[state[j]]
                    break
            return ''.join(state)
    return None

def bts_to_binary(seq):
    return ''.join('1' if c == '0' else '0' for c in seq)

def bts_generate_paths(s, t):
    paths = []
    for sigma in generate_sigma_strings(s, t):
        current = sigma
        path = [current]
        while True:
            next_state = next_bts_state(current)
            if not next_state or next_state in path:
                break
            path.append(next_state)
            current = next_state
        paths.append(path)
    return paths

def find_all_dfs_paths(graph, idx_map):
    all_paths = []
    for start in graph:
        dfs_search([start], {start}, graph, idx_map, all_paths)
    return all_paths

def generate_sigma_strings(s, t):
    total = 2 ** (s - 1)
    sigmas = []
    for i in range(total):
        bits = bin(i)[2:].zfill(s - 1)
        suffix = ''.join('-' if b == '1' else '+' for b in bits)
        sigmas.append('0' * t + '-' + suffix)
    return sigmas


def main():
    parser = argparse.ArgumentParser(description="Γράφος μεταθέσεων με DFS και BTS")
    parser.add_argument("s", type=int, help="Αριθμός μηδενικών")
    parser.add_argument("t", type=int, help="Αριθμός άσσων")
    parser.add_argument("mode", choices=["graph", "dfs", "bts"], help="Λειτουργία: graph, dfs ή bts")
    args = parser.parse_args()
  
