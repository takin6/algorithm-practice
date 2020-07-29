V,E,r = map(int,input().split())
INF = float('inf')
edges = []

for _ in range(E):
  s,d,c = map(int, input().split())
  edges.append([s,d,c])


dist = [INF] * V
dist[r] = 0
for _ in range(V-1):
  for s,d,c in edges:
    if dist[d] > dist[s] + c:
      dist[d] = dist[s] + c

for s,d,c in edges:
  if dist[d] > dist[s] + c:
    print("NEGATIVE CYCLE")
    exit()

for d in dist:
  print(d if d!=INF else "INF")
