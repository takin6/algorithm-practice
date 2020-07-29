N = int(input())
scores = list(map(int, input().split()))

dp = [ [False] * (10000) for _ in range(N+1) ]
dp[0][0] = True

for i in range(N):
  for s in range(10000):
    if s >= scores[i]:
      dp[i+1][s] = dp[i][s] or dp[i][s-scores[i]]
    else:
      dp[i+1][s] = dp[i][s]

print(sum(dp[-1]))
  