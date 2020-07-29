H,W = map(int,input().split())
C = []
for _ in range(10):
  C.append(list(map(int,input().split())))

A = []
for i in range(H):
  A.append(list(map(int,input().split())))

for k in range(10):
  for i in range(10):
    for j in range(10):
      C[i][j] = min(C[i][j], C[i][k]+C[k][j])

ans = 0
for row in A:
  for ele in row:
    if ele != -1:
      ans += C[ele][1]

print(ans)