from itertools import permutations
import argparse
def generate_permutations(s, t):
    base = ['0'] * s + ['1'] * t
    perms = set(permutations(base))  # μοναδικές μεταθέσεις
    bin_strs = [''.join(p) for p in perms]
    index_reprs = [[i for i, bit in enumerate(b) if bit == '1'] for b in bin_strs]
    int_vals = [int(b, 2) for b in bin_strs]
    return bin_strs, index_reprs, int_vals

def main():
    parser = argparse.ArgumentParser(description="Γράφος μεταθέσεων με DFS και BTS")
    parser.add_argument("s", type=int, help="Αριθμός μηδενικών")
    parser.add_argument("t", type=int, help="Αριθμός άσσων")
    parser.add_argument("mode", choices=["graph", "dfs", "bts"], help="Λειτουργία: graph, dfs ή bts")
    args = parser.parse_args()
  
