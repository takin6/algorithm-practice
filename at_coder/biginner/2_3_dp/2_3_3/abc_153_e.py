H, N = map(int, input().split())
# dp = [-1]*(10**4+H)
dp = [float('inf')] * (H+1)

for i in range(N):
  a,b = map(int, input().split())

  for h in range(1, H+1):
    if h-a <= 0:
      dp[h] = min(dp[h], b)
    else:
      dp[h] = min(dp[h], b+dp[h-a])


print(dp[-1])