from operator import mul
from functools import reduce

def cmb(n, r):
  if n < r:
    return 0
  r = min(n - r, r)
  if r == 0:
    return 1
  numer = reduce(mul, range(n, n - r, -1))
  denom = reduce(mul, range(1, r + 1))
  return (numer // denom) % (10 ** 9 + 7)

N,K = map(int,input().split())
MOD = 10**9+7
for i in range(1, K+1):
  print(cmb(K-1,i-1)%MOD * cmb(N-K+1, i)%MOD % MOD)
