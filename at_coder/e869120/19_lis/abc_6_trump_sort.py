import bisect

N = int(input())
A = []
for i in range(N):
  A.append(int(input()))

dp = []
for a in A:
  if len(dp)==0:
    dp.append(a)
  elif a > dp[-1]:
    dp.append(a)
  else:
    pos = bisect.bisect_left(dp, a)
    dp[pos] = a

print(N-len(dp))