N, W = map(int, input().split())
vals, weight = [0], [0]

for _ in range(N):
  v,w = map(int, input().split())
  vals.append(v)
  weight.append(w)

dp = [ [0] * (W+1) for _ in range(N+1)]

for i in range(0, N):
  for w in range(0, W+1):
    if w >= weight[i+1]:
      dp[i+1][w] = max(dp[i][w], dp[i][w-weight[i+1]]+vals[i+1])
    else:
      dp[i+1][w] = dp[i][w]

print(dp[-1][-1])