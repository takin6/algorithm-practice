N,M = map(int, input().split())
edges = []
for _ in range(M):
  u,v,c = map(int, input().split())
  edges.append((-c,u-1,v-1))

INF = float('inf')
dist = [INF] * N
dist[0] = 0
for _ in range(N-1):
  for c,u,v in edges:
    if dist[v] > c+dist[u]:
      dist[v] = c+dist[u]

neg_cycle = [False]*N
for c,u,v in edges:
  if dist[v] > c+dist[u]:
    dist[v] = c+dist[u]
    neg_cycle[u] = True
    neg_cycle[v] = True

if neg_cycle[N-1]:
  print('inf')
else:
  print(-dist[N-1])