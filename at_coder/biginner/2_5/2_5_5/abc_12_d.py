N,M = list(map(int, input().split()))
INF = float('inf')
graph = [ [INF]*N for _ in range(N) ]
for i in range(M):
  u,v,c = map(int,input().split())
  u -= 1
  v -= 1
  graph[u][v] = c
  graph[v][u] = c

for i in range(N): graph[i][i] = 0

for k in range(N):
  for i in range(N):
    for j in range(N):
      graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

res = INF
for i in range(N):
  res = min(res, max(graph[i]))
print(res)
