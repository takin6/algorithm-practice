import heapq

def dijkstra(s,v,t,adj):
  dist = [float('inf')] * (t+1)
  dist[s] = 0
  visited = [False] * (t+1)
  pq = [(0,s)]

  while pq:
    d,n = heapq.heappop(pq)
    visited[n] = True

    for nei,nd in adj[n]:
      if visited[nei]: continue
      if d+nd < dist[nei]:
        dist[nei] = d+nd
        heapq.heappush(pq, (d+nd, nei))

  return dist[v]

n,k = map(int,input().split())
adj = [ [] for _ in range(n+1) ]

for _ in range(k):
  query = list(map(int,input().split()))
  if query[0] == 1:
    adj[query[1]].append((query[2],query[3]))
    adj[query[2]].append((query[1],query[3]))
  else:
    dist = dijkstra(query[1], query[2], n, adj)
    if dist == float('inf'):
      print(-1)
    else:
      print(dist)