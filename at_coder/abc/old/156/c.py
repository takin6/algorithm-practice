from collections import deque

N = int(input())
xs = list(map(int, input().split()))

res = 10**100

avg = sum(xs)//N
mod = sum(xs)%N

for d in range(avg, avg+mod+1):
  r = 0
  for x in xs:
    r += (x-d) ** 2
  res = min(res, r)

print(res)