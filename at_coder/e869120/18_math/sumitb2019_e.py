n = int(input())
A = list(map(int,input().split()))
MOD = 10**9+7

cnt = [0] * (n+1)
cnt[0] = 3

res = 1
for i,a in enumerate(A):
  res *= cnt[a]
  res %= MOD
  cnt[a] -= 1
  cnt[a+1] += 1

print(res % MOD)