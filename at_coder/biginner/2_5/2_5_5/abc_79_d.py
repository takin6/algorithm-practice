H,W = map(int, input().split())
c = []
for i in range(10):
  c.append(list(map(int, input().split())))

A = []
for _ in range(H):
  A.append(list(map(int, input().split())))

for k in range(10):
  for i in range(10):
    for j in range(10):
      c[i][j] = min(c[i][j], c[i][k]+c[k][j])

res = 0
for a in A:
  for e in a:
    if e != -1 and e != 1:
      res += c[e][1]

print(res)