# import sys
# sys.setrecursionlimit(100000)

# 素因数分解
from collections import defaultdict

def factorization(n):
  res = []
  for i in range(2, int(n**0.5//1) + 1):
    if n%i == 0:
      cnt = 0
      while n%i==0:
        n = n//i
        cnt += 1
      res.append([i,cnt])

  if n != 1:
    res.append([n,1])

  return res

N = int(input())
factors = defaultdict(int)
factors[1] = 1
for i in range(2, N+1):
  f = factorization(i)
  for d,cnt in f:
    factors[d] += cnt

mod = 10**9+7
res = 1
for i in range(2, N+1):
  res *= (factors[i]+1)
  res %= mod

print(res)

### prime factorization ####
### 36 = 2^3 * 3^1
# for i in range(2,int(n**0.5)+1):
#   if n%i==0:
#     cnt = 0
#     while n%i==0:
#       n = n//i
#       cnt += 1
#     print(i, cnt)

