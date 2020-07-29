from math import sqrt

N = int(input())
c = []
res = 0
for i in range(N):
  x,y = list(map(int, input().split()))

  for x1,y1 in c:
    res = max(res, sqrt((y1-y)**2 + (x1-x)**2))
  c.append((x,y))

print(res)
