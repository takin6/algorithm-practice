from collections import defaultdict
from heapq import heappush, heappop
N,M,T = map(int,input().split())
A = list(map(int, input().split()))
adj_list = defaultdict(list)
adj_list_reversed = defaultdict(list)
INF = 10**100

def dijkstra(g):
  visited = [False]*N
  times = [INF] *N
  times[0] = 0
  pq = [(0, 0)]

  while pq:
    t,n = heappop(pq)
    visited[n] = True
    for nei,nt in g[n]:
      if visited[nei]: continue
      if t+nt < times[nei]:
        times[nei] = t+nt
        heappush(pq, (t+nt,nei))
  return times

for _ in range(M):
  a,b,c = map(int,input().split())
  a -= 1
  b -= 1
  adj_list[a].append((b,c))
  adj_list_reversed[b].append((a,c))

departing = dijkstra(adj_list)
returning = dijkstra(adj_list_reversed)

res = -INF
for i in range(N):
  res = max(res, A[i]*(T-departing[i]-returning[i]))

print(res)