# knapsack = weight, val, capacity
# maximize val within the capacity

# Bを最大化。T分以内
# 

N,T = map(int,input().split())
foods = []
for _ in range(N):
  a,b = map(int,input().split())
  foods.append([a,b])

foods.sort(key=lambda x: x[0])

# dp[i][j] = 1～i 番目の料理で j 分以内に完食できる美味しさの合計の最大値
dp = [ [0]*(T+1) for _ in range(N+1) ]

for i in range(N):
  a,b = foods[i]
  for j in range(T+1):
    if j >= a:
      dp[i+1][j] = max(dp[i][j], dp[i][j-a]+b)
    else:
      dp[i+1][j] = dp[i][j]

# for d in dp:
#   print(d)

ans = 0
for i in range(1, N+1):
  b = foods[i-1][1]
  ans = max(ans, dp[i][-1], dp[i-1][-2]+b)

print(max(ans, dp[-1][-1]))

  # prev_a,prev_b = foods[i]
  # last = dp[i].index(0)
  # for j in range(last+1, min(T, prev_a+a+1)):
  #   dp[i+1][j] = dp[i][j] + prev_b +  b

  # for j in range(T):
  #   dp[i+1][j] = max(dp[i+1][j], dp[i][j])

