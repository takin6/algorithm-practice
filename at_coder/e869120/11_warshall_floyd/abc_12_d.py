N,M = map(int,input().split())
matrix = [ [float('inf')]*N for _ in range(N)  ]
for i in range(N):
  matrix[i][i] = 0

for _ in range(M):
  u,v,t = map(int,input().split())
  u -= 1
  v -= 1
  matrix[u][v] = t
  matrix[v][u] = t

for k in range(N):
  for i in range(N):
    for j in range(N):
      matrix[i][j] = min(matrix[i][j], matrix[i][k]+matrix[k][j])

res = float('inf')
for i in range(N):
  res = min(res, max(matrix[i]))

print(res)

# for i in range(N-1):
#   res = min(res, matrix[i][N-1])