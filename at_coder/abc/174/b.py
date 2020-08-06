import math

N,D = map(int,input().split())

ans = 0
for _ in range(N):
  x,y = map(int,input().split())
  dist = math.sqrt(x**2 + y**2)
  if dist <= D:
    ans += 1

print(ans)