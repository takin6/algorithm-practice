from collections import Counter
import math
N = int(input())
xy = []
for _ in range(N):
  xy.append(tuple(map(int,input().split())))
setxy = set(xy)

# (1,1),(4,0) => (3,1)
# (1,1),(2,4) => (1,3)
ans = 0

for i in range(N):
  x,y = xy[i]
  for j in range(i+1, N):
    x2,y2 = xy[j]
    vx,vy = x2-x, y2-y
    if (x-vy,y+vx) in setxy and (x2-vy,y2+vx) in xy:
      ans = max(ans, vx**2+vy**2)

print(ans)