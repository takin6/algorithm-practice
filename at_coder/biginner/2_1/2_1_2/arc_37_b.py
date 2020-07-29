from collections import defaultdict
N,M = list(map(int, input().split()))
adj_list = defaultdict(list)

for _ in range(M):
  u,v = list(map(int, input().split()))
  adj_list[u].append(v)
  adj_list[v].append(u)

visited = []
cycle = 0

def dfs(f, node, has_cycle):
  visited.append(node)

  for neighbor in adj_list[node]:
    if neighbor == f: continue
    elif neighbor in visited:
      return True
    else:
      has_cycle = dfs(node, neighbor, has_cycle)

  return has_cycle

cycle = 0
for i in range(1, N+1):
  if i not in visited:
    if not dfs(-1, i, False):
      cycle += 1

print(cycle)