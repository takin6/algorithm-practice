from collections import defaultdict
import heapq
N,E,S = map(int, input().split())
adj_list = defaultdict(list)

for _ in range(E):
  s,t,d = map(int, input().split())
  adj_list[s].append((t,d))

def dijkstra():
  visited = [False] * (N)
  dist = [float('inf')] * (N)
  dist[S] = 0

  pq = [(0,S)]
  heapq.heapify(pq)
  while pq:
    curDist,node = heapq.heappop(pq)
    visited[node] = True
    for nei, nc in adj_list[node]:
      if visited[nei]: continue
      newDist = curDist + nc
      if newDist < dist[nei]:
        dist[nei] = newDist
        heapq.heappush(pq, (newDist,nei))

  return dist

dist = dijkstra()
for d in dist:
  if d == float('inf'):
    print("INF")
  else:
    print(d)