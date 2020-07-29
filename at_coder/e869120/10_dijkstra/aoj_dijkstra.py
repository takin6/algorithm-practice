import heapq
V,E,r = map(int,input().split())
adj = [ [] for _ in range(V) ]

for _ in range(E):
  u,v,w = map(int,input().split())
  adj[u].append((v,w))

def dijkstra():
  dist = [float('inf')] * V
  dist[r] = 0
  visited = [False] * V

  pq = [(0,r)]
  while pq:
    w,n = heapq.heappop(pq)
    visited[n] = True

    for nei,wei in adj[n]:
      if visited[nei]: continue
      if w+wei < dist[nei]:
        dist[nei] = w+wei
        heapq.heappush(pq, (w+wei, nei))

  return dist

for d in dijkstra():
  if d == float('inf'):
    print("INF")
  else:
    print(d)

