from itertools import permutations
import argparse

def main():
    parser = argparse.ArgumentParser(description="Γράφος μεταθέσεων με DFS και BTS")
    parser.add_argument("s", type=int, help="Αριθμός μηδενικών")
    parser.add_argument("t", type=int, help="Αριθμός άσσων")
    parser.add_argument("mode", choices=["graph", "dfs", "bts"], help="Λειτουργία: graph, dfs ή bts")
    args = parser.parse_args()
  
