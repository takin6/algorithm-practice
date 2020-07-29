N,W = map(int,input().split())
vals, weis = [], []

for _ in range(N):
  v,w = map(int, input().split())
  vals.append(v)
  weis.append(w)

dp = [ [0]*(W+1) for _ in range(N+1)]

for i in range(1, N+1):
  for w in range(1, W+1):
    if w >= weis[i-1]:
      dp[i][w] = max(dp[i][w-weis[i-1]]+vals[i-1], dp[i-1][w])
    else:
      dp[i][w] = dp[i-1][w]

print(dp[-1][-1])
