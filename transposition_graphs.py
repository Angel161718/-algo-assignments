import argparse
from itertools import permutations

def parse_arguments():
  parser = argparse.ArgumentParser(description = "Transposition Graphs")
  parser.add_argument('s', type = int, help = 'Αριθμός Μηδενικών (0)')  
  parser.add_argument('t', type = int, help ='Αριθμός Μοναδών (1)')
  parser.add_argument('mode', choises = ['graph', 'dfs', 'bts'], help = 'Λειτουργεία')
  parser.add_argument('start', nargs = '?', type = int, help = 'Προαιρετικός κόμβος εκκίνησης για DFS')
  return parser.parse_args()

def generate_permutations(s, t):
  initial = ['0'] * s + ['1'] * t
  all_perms = set(permutations(initial))
  binary_strs = [''.join(p) for p in all_perms]
  int_vals = [int(b,2) for b in binary_strs]
  index_reprs = [[i for i, bit in enumerate(b) if bit == '1'] for
  return binary_strs, index_reprs, int_vals

def build_graph(bin_strs):
  graph = {}
  perm_set = set(bin_strs)

for b in bin_strs:
  neighbors = []
  b_list = list(b)
  for i in range(len(b_list)):
    for j in range(i + 1, len(b_list)):
      if b_list[i] != b_list[j]:
        b_list[i], b_list[j] = b_list[j], b_list[i]
        swapped = ''.join(b_list)
        if swapped in perm_set:
          neighbors.append(int(swapped, 2))
        b_list[i], b_list[j] = b_list[j], b_list[i]
    graph[int(b, 2)] = sorted(set(neighbors))
  return graph

def  is_genlex_path(index_paths):
  for i in range(len(index_paths) - 1):
    prefix = index_paths[i] 
    next_prefix = index_paths[i + 1] [:len(prefix)]
    if prefix != next_prefix:
      return False
  return True

def hamming_index_distance(a, b):
  return sum(x != y for x,y in zip(a,b))

def dfs_search(path, visisted, graph, idx_map, all_paths):
  if len(visited) == len(graph):
    all_paths.append(path[:])
    return
  current = path[-1]
  for neighbor in graph[current]:
    if neighbor not in visited:
      new_path = path + [neighbor]
      if is_genlex_path([idx_map[p] for p in new_path]) and \ 
        hamming_index_distance(idx_map[current], idx_map[neighbor]) == 1:
          visited.add(neighbor)
          dfs_search(new_path, visited, graph, idx_map, all_paths)
          visited.remove(neighbor)

def find_all_dfs_paths(graph, idx_map):
  all_paths = []
  for start in graph:
    dfs_search([start], {start}, graph, idx_map, all_paths)
  return all_paths

def print_path(path, length):
  binaries = [format(n, f"0{length}b") for n in path]
  print(" ", binaries)
  indices = ["".join(map(str, [i for i in range(length) if (n >> (length - i - 1)) & 1])) for in path]
  print("", indices)
  print("", path)
                               
def generate_sigma_j(j,s,t):
  bin_j = format(j, f"0{s-1}b")
  suffix = ''.join('-' if bit == '1' else '+' for bit in bin_j)
  return'0' * t + suffix

def next_bts_strings(s):
  chars = list(s)
  i = len(chars) - 1
  while i > 0:
    if chars[i] == '+' and chars[i-1] == '-':
        chars[i-1] = '0'
        chars[i] = '-'
        break
    elif chars[i] == '-' and chars[i-1] == '+':
      chars[i-1] = '0'
      chars[i] = '+'
      break
      i -= 1
  else:
    return None
  return ''.join(chars)

def ternary_to_binary(tstr):
  return ''.join('1' if c == '0' else '0' for c in tstr)

def bts_walk(s, t):
  all_paths = []
  length = s + t 
  for j in range(2 ** (s - 1)):
    bts_chain = []
    current = generate_sigma_j(j, s, t)
    while current: 
      bts_chain.append(current)
      current = next_bts_string(current)
    all_paths.append(bts_chain)
  return all_paths

def main():
  args  = parse_arguments()
  s, t, mode, start = args.s, args.t, args.mode, args.start
  length = s + t

  bin_strs, index_reprs, int_vals = generate_permutations(s, t)
  graph = build_graph(bin_strs)
  idx_map = {int_vals[i]: index-reprs[i] for i in range(len(int_vals))}

  
  


    


  

        
    
