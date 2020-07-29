H,N = map(int,input().split())
INF = float('inf')
# dp[i] = 攻撃がh以上となるときに考えられる最小の体力消耗
dp = [INF] * (H+1)

for _ in range(N):
  a,b = map(int,input().split())

  for h in range(1, H+1):
    if h <= a:
      dp[h] = min(dp[h],b)
    else:
      dp[h] = min(dp[h],dp[h-a]+b)

print(dp[-1])