# ### answer ###
# S = input()[::-1]
# L = len(S)
# N = 13
# mod = 1000000007

# dp= [0] * N
# dp[0] = 1
# mul = 1
# for i in range(L):
#   nextDP = [0] * N
#   c = S[i]
#   if c == "?":
#     # 次の桁
#     for k in range(10):
#       # 前の桁の13で割ったあまり
#       for j in range(N):
#         nextDP[(k*mul+j)%N] += dp[j]
#         nextDP[(k*mul+j)%N] %= mod
#   else:
#     k = int(c)
#     for j in range(N):
#       nextDP[(k*mul+j)%N] += dp[j]
#       nextDP[(k*mul+j)%N] %= mod

#   mul *= 10
#   mul %= N
#   dp = nextDP

# print(dp[5])


S = input()[::-1]
L = len(S)
MOD = 10**9+7
N = 13
# 0~13
dp = [ [0]*13 for i in range(L+1)]
dp[0][0] = 1
mul = 1

for i in range(L):
  if S[i] == "?":
    for prev in range(N):
      for j in range(10):
        dp[i+1][(j*mul+prev)%N] += dp[i][prev]
        dp[i+1][(j*mul+prev)%N] %= MOD
  else:
    j = int(S[i])
    for prev in range(N):
      dp[i+1][(j*mul+prev)%N] += dp[i][prev]
      dp[i+1][(j*mul+prev)%N] %= MOD
  
  mul *= 10
  mul %= N

print(dp[-1][5])