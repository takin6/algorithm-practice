from math import gcd
N = int(input())
res = 0
for i in range(1, N+1):
  for j in range(1, N+1):
    g = gcd(i,j)
    for k in range(1, N+1):
      res += gcd(g, k)
print(res)