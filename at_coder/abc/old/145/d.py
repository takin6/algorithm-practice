# X,Y = map(int,input().split())
# INF = 10**15
# MOD = 10**9+7
# dp = [ [INF]*(Y+1) for _ in range(X+1) ]
# dp[0][0] = 1

# for i in range(X):
#   for j in range(Y):
#     if dp[i][j] != INF:
#       if i+1<=X and j+2<=Y:
#         if dp[i+1][j+2] == INF:
#           dp[i+1][j+2] = dp[i][j]
#           dp[i+1][j+2] %= MOD
#         else:
#           dp[i+1][j+2] += 1
#           dp[i+1][j+2] %= MOD
      
#       if i+2<=X and j+1<=Y:
#         if dp[i+2][j+1] == INF:
#           dp[i+2][j+1] = dp[i][j]
#           dp[i+2][j+1] %= MOD
#         else:
#           dp[i+2][j+1] += 1
#           dp[i+2][j+1] %= MOD

# print(dp)
# print(dp[-1][-1])

# [[1, 1000000000000000, 1000000000000000], 
# [1000000000000000, 1000000000000000, 1], 
# [1000000000000000, 1, 1000000000000000]]


def nCr(n,r):
  dividend,divisor = 1,1
  for i in range(r):
    dividend *= n-i
    divisor *= 1+i
    dividend %= MOD
    divisor %= MOD

  return (dividend * pow(divisor, MOD-2, MOD)) % MOD

X,Y = map(int,input().split())
INF = 10**15
MOD = 10**9+7

if (X+Y)%3!=0:
  print(0)
  exit()

n = (-X + 2*Y) // 3
m = (2*X - Y) // 3

if n<0 or m<0:
  print(0)
  exit()

print(nCr(n+m, n))