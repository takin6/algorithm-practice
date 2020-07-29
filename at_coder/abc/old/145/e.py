# N,T = map(int,input().split())
# food = []
# for _ in range(N):
#   food.append(list(map(int,input().split())))
# food.sort(key= lambda x: x[0])

# MIN_INF = -float('inf')
# dp = [ [MIN_INF]*(T+1) for _ in range(N) ]
# dp[0][0] = 0

# for i in range(1,N):
#   for t in range(T+1):
#     a,b = food[i-1]
#     if t-a >= 0:
#       dp[i][t] = max(dp[i][t], dp[i-1][t-a]+b)
#     dp[i][t] = max(dp[i][t], dp[i-1][t])
#     print(i,t,dp[i][t])


def knapsack(n, w, food):
  dp = [[0]*(w + 1) for i in range(n + 1)]

  for i in range(n):
    for j in range(w + 1):
      weight, value = food[i]
      if j < weight:
        dp[i + 1][j] = dp[i][j]
      else:
        dp[i + 1][j] = max(dp[i][j], dp[i][j - weight] + value)

  return dp

N,T = map(int,input().split())
food = []
for _ in range(N):
  food.append(list(map(int,input().split())))
food.sort(key= lambda x: x[0])
dp = knapsack(N,T,food)

C = [0]*(N+1)
for i in range(N)[::-1]:
  C[i] = max(C[i+1], food[i][1])

ans = 0
for i in range(N+1):
  ans = max(dp[i][-2] + C[i], ans)

print(ans)


# a,b = food[-1]
# import pdb; pdb.set_trace()
# print(max( max(dp[-1][:T])+b,  dp[-1][T] ))
# # a,b = food[-1]
# # # 最後を選ぶか選ばないか
# # for i in range(T):
# #   dp[-1]

# [[13, 17], 
# [15, 23], 
# [18, 29], 
# [18, 20], 
# [19, 27], 
# [20, 18], 
# [22, 25], 
# [23, 21], 
# [24, 12],
# [27, 15]]