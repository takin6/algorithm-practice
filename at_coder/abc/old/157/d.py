from collections import defaultdict

# def dfs(cur_node, candidates, visited, cnt, direct_rel):
#   if len(candidates) == 0: return cnt

#   for node, status in candidates:
#     if visited[node] == True: continue
#     # if (node, status) in direct_rel: continue

#     visited[node] = True

#     if status == FRIEND:
#       if node not in direct_rel:
#         cnt += 1
#       print(cur_node, (node, status), cnt)
#       return dfs(cur_node, adj_list[node], visited,  cnt, direct_rel)

#   return cnt

def dfs(cur_node, candidates, visited, level, cnt):

  while len(candidates) > 0:
    node, level = candidates.pop(0)

    if visited[node]: continue
    visited[node] = True

    if level > 0: cnt += 1

    for n in adj_list[node][FRIEND]:
      if n in adj_list[cur_node][BLOCK]:
        candidates.append((n, 0))
      if visited[n] == False:
        candidates.append((n, level+1))

  return cnt

# -----------------------------------------

FRIEND, BLOCK = 0, 1

N, F, B = list(map(int, input().split()))
adj_list = defaultdict(dict)
for i in range(1, N+1):
  adj_list[i][0] = set()
  adj_list[i][1] = set()

for _ in range(F):
  u, v = list(map(int, input().split()))
  adj_list[u][FRIEND].add(v)
  adj_list[v][FRIEND].add(u)

for _ in range(B):
  u, v = list(map(int, input().split()))
  adj_list[u][BLOCK].add(v)
  adj_list[v][BLOCK].add(u)

ans = []

for i in range(1, N+1):
  visited = [False] * (N+1)
  visited[i] = True
  candidates = []
  for node in adj_list[i][FRIEND]:
    # if status == FRIEND:
    # node, level
    candidates.append((node, 0))

  cnt = 0
  cnt = dfs(i, candidates, visited, 0, 0)
  ans.append(cnt)

print(*ans)

print(" ".join([str(i) for i in ans]))


  # visited = [False] * (N+1) 
  # candidates = []
  # direct_rel = []

  # visited[i] = True
  # # pass direct relationship
  # for node, status in adj_list[i]:
  #   # visited[node] = True
  #   # direct_rel.append((node, status))
  #   direct_rel.append(node)

  #   if status == FRIEND and node != i:
  #     for node in adj_list[node]:
  #       candidates.append(node)

  # cnt = 0
  # if len(candidates) > 0:
  #   cnt = dfs(i, candidates, visited, 0, direct_rel)
  # ans.append(cnt)