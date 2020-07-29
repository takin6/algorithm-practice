# import sys
# sys.setrecursionlimit(10**6)
# N,M = map(int,input().split())
# A = []
# MOD = 10**9+7
# memo = {}
# for _ in range(M):
#   memo[a] = 0

# def step(cur):
#   if cur in memo:
#     return memo[cur]
#   if cur == N:
#     memo[cur] = 1
#     return memo[cur]
#   if cur > N:
#     memo[cur] = 0
#     return memo[cur]
 
#   memo[cur] = (step(cur+1) + step(cur+2))%MOD
#   return memo[cur]
 
# print(step(0)%MOD)

N,M = map(int,input().split())
MOD = 10**9+7
dp = [0] * (N+1)
dp[1] = 1
for _ in range(M):
  dp[int(input())] = -1
if N<2:
  print(dp[N])
  exit()

if dp[2] != -1:
  dp[2] = 1
for i in range(N+1):
  if dp[i] == -1: continue
  if i-1>=0 and dp[i-1] != -1:
    dp[i] += dp[i-1]
  if i-2>=0 and dp[i-2] != -1:
    dp[i] += dp[i-2]
  dp[i] %= MOD

print(dp[N])
# dp[i][j] = i回目にjにたどり着ける回数(N**10)
# dp = [0] * 

# 0 1 2 3
# 0 1 3
# 0 2 3
