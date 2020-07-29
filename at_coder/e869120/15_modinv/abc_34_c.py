def nCr(n,r):
  MOD = 10**9+7
  dividend, divisor = 1,1
  d1 = n
  for i in range(1,r+1):
    dividend *= d1
    divisor *= i
    dividend %= MOD
    divisor %= MOD
    d1 -= 1

  return (dividend * pow(divisor, MOD-2, MOD)) % MOD

W,H = map(int,input().split())
print(nCr(W-1+H-1, W-1))
