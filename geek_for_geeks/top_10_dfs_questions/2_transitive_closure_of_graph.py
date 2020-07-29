from collections import defaultdict

n = 4
edge_list = [[0, 1],[0,2], [1,2], [2,3], [2, 0], [3, 3]]

adj_list =  defaultdict(set)
for u, v in edge_list: adj_list[u].add(v)
print(adj_list)

tc = [[0 for j in range(n)] for i in range(n)] 

def dfs(s, v):
  print(s, v)
  tc[s][v] = 1

  for neighbor in adj_list[v]:
    if tc[s][neighbor] == 0:
      dfs(s, neighbor)

for i in range(n): dfs(i, i)
print(tc)