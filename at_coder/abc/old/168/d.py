from collections import deque
import heapq
N,M = map(int,input().split())
adj = [ [] for _ in range(N+1) ]
for _ in range(M):
  a,b = map(int,input().split())
  adj[a].append(b)
  adj[b].append(a)

def dijkstra(N):
  signs = [None] * (N+1)
  signs[0] = -1
  steps = [float('inf')] * (N+1)
  visited = [False] * (N+1)

  # step,from,cur_node
  q = [(0, -1, 1)]
  while q:
    step,p,cur_node = heapq.heappop(q)
    steps[cur_node] = step
    signs[cur_node] = p
    visited[cur_node] = True

    for nei in adj[cur_node]:
      if visited[nei]: continue
      if step+1 < steps[nei]:
        steps[nei] = step+1
        heapq.heappush(q, (step+1, cur_node, nei))
  return signs

signs = dijkstra(N)[2:]
if float('inf') in signs:
  print("No")
else:
  print("Yes")
  for s in signs:
    print(s)

# print("Yes")
# for e in res: print(e)