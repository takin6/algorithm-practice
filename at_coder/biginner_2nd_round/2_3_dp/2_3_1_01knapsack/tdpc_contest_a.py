N = int(input())
P = list(map(int,input().split()))
S = sum(P)
dp = [-1]*(S+1)
dp[0] = 1

for i in range(N):
  for s in range(S, -1, -1):
    if s-P[i]>=0 and dp[s-P[i]] >= 0:
      dp[s] = 1

print(dp.count(1))