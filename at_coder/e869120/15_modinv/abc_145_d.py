# n + 2n
# 2m + m
# (n + 2m) = X
# (2n + m) = Y
def nCr(n,r):
  dividend = 1
  divisor = 1
  MOD = 10**9+7
  d1 = n
  for i in range(1,r+1):
    dividend *= d1
    divisor *= i
    d1 -= 1
    dividend %= MOD
    divisor %= MOD

  return (dividend * pow(divisor, MOD-2, MOD)) % MOD

X,Y = map(int,input().split())

if (X+Y) % 3 != 0:
  print(0)
  exit()

n = (-X+2*Y) // 3
m = (2*X-Y) // 3

if n<0 or m<0:
  print(0)
else:
  print(nCr(n+m, n))