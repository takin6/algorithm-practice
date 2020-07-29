N,W = map(int,input().split())
dp = [ [0]*(W+1) for _ in range(N+1) ]
vals = []
weights = []
for _ in range(N):
  v,w = map(int,input().split())
  vals.append(v)
  weights.append(w) 

for i in range(1, N+1):
  for w in range(1, W+1):
    if weights[i-1] <= w:
      dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]]+vals[i-1])
    else:
      dp[i][w] = max(dp[i-1][w], dp[i][w-1])

print(dp[-1][-1])