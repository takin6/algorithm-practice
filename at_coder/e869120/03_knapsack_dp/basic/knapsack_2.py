N,W = map(int,input().split())
items = []
for i in range(N):
  items.append(list(map(int,input().split())))

dp = [ [0]*(W+1) for _ in range(N+1) ]
for i in range(1, N+1):
  val,wei = items[i-1]
  for w in range(W+1):
    if w >= wei:
      dp[i][w] = max(dp[i-1][w], dp[i][w-wei]+val)
    else:
      dp[i][w] = max(dp[i-1][w], dp[i][w-1])

print(dp[N][W])