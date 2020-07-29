V,E = map(int,input().split())
INF = float('inf')
graph = [ [INF]*V for _ in range(V) ]

for _ in range(E):
  s,d,c = map(int, input().split())
  graph[s][d] = c

for i in range(V):
  graph[i][i] = 0

for k in range(V):
  for i in range(V):
    for j in range(V):
      if graph[i][j] > graph[i][k] + graph[k][j]:
        graph[i][j] = graph[i][k] + graph[k][j]

for i in range(V):
  if graph[i][i] < 0:
    print('NEGATIVE CYCLE')
    exit()

for g in graph:
  print(" ".join(map(str, [ e if e!=INF else "INF" for e in g ])))
