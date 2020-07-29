V,E = map(int,input().split())
matrix = [ [float('inf')]*V for _ in range(V) ]

for i in range(V):
  matrix[i][i] = 0

for _ in range(E):
  u,v,w = map(int,input().split())
  matrix[u][v] = w

for k in range(V):
  for i in range(V):
    for j in range(V):
      matrix[i][j] = min(matrix[i][j], matrix[i][k]+matrix[k][j])

for i in range(V):
  if matrix[i][i] < 0:
    print("NEGATIVE CYCLE")
    exit()


for i in range(V):
  print(" ".join(map(str, [ "INF" if e==float('inf') else e for e in matrix[i] ])))