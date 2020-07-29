def nCr(n,r):
  dividend, divisor = 1,1
  MOD = 10**9+7
  for i in range(r):
    dividend *= (n-i)
    divisor *= (1+i)
    dividend %= MOD
    divisor %= MOD
  return (dividend * pow(divisor, MOD-2, MOD))%MOD

n = int(input())
k = int(input())

print(nCr(n+k-1, k))

# hako = k, ball = n
# print(kHn(k,n))