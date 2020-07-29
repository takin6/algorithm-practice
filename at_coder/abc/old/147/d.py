N = int(input())
A = list(map(int,input().split()))
mod = 10**9+7
res = 0
for i in range(61):
  zeros, ones = 0, 0
  for a in A:
    if (a>>i)&1:
      ones += 1
    else:
      zeros += 1
  res += (zeros*ones) * (1<<i)
  res %= mod

print(res)

# XORは桁を独立して考える