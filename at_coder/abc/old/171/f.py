# nCr
def calcComb(n,r):
  mul, div = 1, 1
  for i in range(r):
    mul *= (n-i)
    div *= (i+1)
    mul %= mod
    div %= mod
  return mul * pow(div,mod-2,mod) % mod

K = int(input())
S = input()
mod = 10**9+7