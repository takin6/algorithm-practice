N,W = map(int,input().split())
weights,vals = [],[]
for _ in range(N):
  v,w = map(int,input().split())
  weights.append(w)
  vals.append(v)

dp = [ [0]*(W+1) for _ in range(N+1) ]

for i in range(1, N+1):
  for w in range(1,W+1):
    if w >= weights[i-1]:
      dp[i][w] = max(dp[i][w], dp[i-1][w], dp[i-1][w-weights[i-1]]+vals[i-1], dp[i][w-weights[i-1]]+vals[i-1])
    else:
      dp[i][w] = max(dp[i][w], dp[i][w-1], dp[i-1][w])

print(dp)
print(dp[-1][-1])