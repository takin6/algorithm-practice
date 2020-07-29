import heapq

N,M,T = map(int,input().split())
A = list(map(int,input().split()))

adj = [[] for _ in range(N) ]
adj_reverse = [[] for _ in range(N) ]

for _ in range(M):
  u,v,t = map(int,input().split())
  u -= 1
  v -= 1
  adj[u].append((v,t))
  adj_reverse[v].append((u,t))

def dijkstra(g):
  dist = [float('inf')] * N
  visited = [False] * N
  dist[0] = 0

  q = [(0,0)]
  while q:
    d,n = heapq.heappop(q)
    visited[n] = True
    for nei, nd in g[n]:
      if visited[nei]: continue
      if nd+d < dist[nei]:
        dist[nei] = nd+d
        heapq.heappush(q, (dist[nei], nei))

  return dist

lst1,lst2 = dijkstra(adj),dijkstra(adj_reverse)
res = -10**15
for i in range(N):
  res = max(res, A[i]*(T-lst1[i]-lst2[i]))

print(res)